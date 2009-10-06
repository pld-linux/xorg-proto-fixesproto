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
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Fixes extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia X Fixes.

%package devel
Summary:	X Fixes extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia X Fixes
Group:		X11/Development/Libraries
Requires:	xorg-proto-xextproto-devel >= 1:7.1.0
Requires:	xorg-proto-xproto-devel
Obsoletes:	fixesext

%description devel
X Fixes extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia X Fixes.

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
%doc COPYING ChangeLog fixesproto.txt
%{_includedir}/X11/extensions/xfixes*.h
%{_pkgconfigdir}/fixesproto.pc
