Summary:	A Dockable General Purpose Recording Utility
Summary(pl):	Dokowalne Narzędzie do Nagrywania
Name:		wmrecord
Version:	1.0.5
Release:	1
Copyright:      GPL
Group:          X11/Window Managers/Tools
Group(pl):	X11/Zarządcy Okien/Narzędzia
Source0:	http://www.bruhaha.demon.co.uk/%{name}-%{version}.tar.gz
Source1:	wmrecord.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
WMRecord is a general purpose audio recording utility for X11, currently 
using the Open Sound System (OSS). The interface is designed to work in 
conjunction with WindowMaker's Dock or AfterStep's Wharf, two popular 
window managers for the X Window System. 

%description -l pl
WMRecord jest narzędziem nagrywającym dla środowiska X11, w obecnej
chwili wykorzystującym sterowniki Open Sound System (OSS).
Interfejs programu jest zaprojektowany do pracy w połączeniu z Dokiem
WindowMakera lub AfterStepa.

%prep
%setup -q

%build

make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install man/wmrecord.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -s wmrecord $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README TODO Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,Changelog}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/DockApplets/wmrecord.desktop
