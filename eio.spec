#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Enlightenment Input Output Library
Summary(pl.UTF-8):	Enlightenment Input Output - biblioteka wejścia/wyjścia z projektu Enlightenment
Name:		eio
Version:	0.1.0.65643
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
# Source0-md5:	244d07702020c919a6f99b2b1856da9a
URL:		http://trac.enlightenment.org/e/wiki/Eio
BuildRequires:	eina-devel >= 1.0.0
BuildRequires:	ecore-devel >= 1.0.0
BuildRequires:	pkgconfig >= 1:0.22
Requires:	eina >= 1.0.0
Requires:	ecore >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended to provide non blocking I/O by using thread
for all operation that may block. It depends only on eina and ecore
right now. It should integrate all the features/functions of
Ecore_File that could block.

%description -l pl.UTF-8
Ta biblioteka na za zadanie zapewniać nieblokujące operacje we/wy
poprzez użycie wątków dla wszystkich operacji, które mogę być
blokujące. Na razie wymaga tylko bibliotek eina i ecore. Powinna
zawierać wszystkie funkcje Ecore_File, które mogą być blokujące.

%package devel
Summary:	Header files for Eio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Eio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	eina-devel >= 1.0.0
Requires:	ecore-devel >= 1.0.0

%description devel
Header files for Eio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Eio.

%package static
Summary:	Static Eio library
Summary(pl.UTF-8):	Statyczna biblioteka Eio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Eio library.

%description static -l pl.UTF-8
Statyczna biblioteka Eio.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libeio-ver-pre-svn-09.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeio-ver-pre-svn-09.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeio.so
%{_libdir}/libeio.la
%{_includedir}/eio-0
%{_pkgconfigdir}/eio.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libeio.a
%endif
