# $Rev: 3264 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	Fixes protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fixes i pomocnicze
Name:		xorg-proto-fixesproto
Version:	3.0
Release:	0.03
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/fixesproto-%{version}.tar.bz2
# Source0-md5:	001a51cca8e764e362fe98e61c22d54e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/fixesproto-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%description devel
Fixes protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Fixes i pomocnicze.


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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/fixesproto.pc
