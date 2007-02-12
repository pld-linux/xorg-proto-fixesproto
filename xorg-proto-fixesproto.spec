Summary:	Fixes protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Fixes i pomocnicze
Name:		xorg-proto-fixesproto
Version:	4.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/fixesproto-%{version}.tar.bz2
# Source0-md5:	8b298cc3424597f8138c7faf7763dce9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixes protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Fixes i pomocnicze.

%package devel
Summary:	Fixes protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Fixes i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xextproto-devel
Requires:	xorg-proto-xproto-devel
Obsoletes:	fixesext

%description devel
Fixes protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Fixes i pomocnicze.

%prep
%setup -q -n fixesproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/fixesproto.pc
