%{?scl:%scl_package libsass}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}libsass
Version:        3.3.6
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
%{?scl:scl enable %{scl} "}
%setup -q
autoreconf --force --install
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
%configure --disable-static \
           --disable-tests \
           --enable-shared

make %{?_smp_mflags}
%{scl:"}

%install
%{?scl:scl enable %{scl} "}
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%{?scl:"}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc Readme.md LICENSE
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Feb 10 2015 Gawain Lynch <gawain.lynch@gmail.com> - 3.1.0-1
- Initial SPEC file

