Summary:	X Fixes extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia X Fixes
Name:		xorg-proto-fixesproto
Version:	4.1.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/fixesproto-%{version}.tar.bz2
# Source0-md5:	4c1cb4f2ed9f34de59f2f04783ca9483
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header files and documentation for the XFIXES extension.

%description -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do rozszerzenia XFIXES.

%package devel
Summary:	X Fixes extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia X Fixes
Group:		X11/Development/Libraries
Requires:	xorg-proto-xextproto-devel >= 1:7.1.0
Requires:	xorg-proto-xproto-devel
Obsoletes:	fixesext

%description devel
Header files and documentation for the XFIXES extension.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do rozszerzenia XFIXES.

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
%doc COPYING ChangeLog README fixesproto.txt
%{_includedir}/X11/extensions/xfixes*.h
%{_pkgconfigdir}/fixesproto.pc
