%{?scl:%scl_package libsass}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}libsass
Version:        3.4.5
Release:        1%{?dist}
Summary:        A C/C++ implementation of a Sass compiler

License:        MIT
URL:            http://libsass.org
Source0:        https://github.com/sass/%{name}/archive/%{version}.tar.gz

BuildRequires:  %{?scl_prefix}gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%if 0%{?rhel} < 7
Patch0:         01-autoconfig.patch
%endif

%description
LibSass is a C/C++ port of the Sass engine. The point is to be simple, fast, and easy to integrate.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{pkg_name}-%{version}

%if 0%{?rhel} < 7
%patch0 -p1
%endif

%{?scl:scl enable %{scl} - << \EOF}
set -e
autoreconf --force --install
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
set -e
%configure --enable-static \
           --disable-tests \
           --enable-shared

make %{?_smp_mflags}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%{?scl:EOF}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc Readme.md LICENSE
%{_libdir}/*.so.*
%{_libdir}/*.a

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Feb 10 2015 Gawain Lynch <gawain.lynch@gmail.com> - 3.1.0-1
- Initial SPEC file

