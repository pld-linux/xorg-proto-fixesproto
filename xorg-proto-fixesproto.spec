Summary:	Fixes protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fixes i pomocnicze
Name:		xorg-proto-fixesproto
Version:	3.0.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/fixesproto-X11R7.0-%{version}.tar.bz2
# Source0-md5:	ff8899d2325ed8a5787cde372ca8f80f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixes protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Fixes i pomocnicze.

%package devel
Summary:	Fixes protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fixes i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xextproto-devel
Requires:	xorg-proto-xproto-devel
Obsoletes:	fixesext

%description devel
Fixes protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Fixes i pomocnicze.

%prep
%setup -q -n fixesproto-X11R7.0-%{version}

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
