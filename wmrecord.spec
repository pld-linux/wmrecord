Summary:	A Dockable General Purpose Recording Utility
Summary(pl):	Dokowalne Narzêdzie do Nagrywania
Name:		wmrecord
Version:	1.0.5
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.bruhaha.co.uk/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.bruhaha.co.uk/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
WMRecord is a general purpose audio recording utility for X11,
currently using the Open Sound System (OSS). The interface is designed
to work in conjunction with WindowMaker's Dock or AfterStep's Wharf,
two popular window managers for the X Window System.

%description -l pl
WMRecord jest narzêdziem nagrywaj±cym dla ¶rodowiska X11, w obecnej
chwili wykorzystuj±cym sterowniki Open Sound System (OSS). Interfejs
programu jest zaprojektowany do pracy w po³±czeniu z Dokiem
WindowMakera lub AfterStepa.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install man/wmrecord.1 $RPM_BUILD_ROOT%{_mandir}/man1
install wmrecord $RPM_BUILD_ROOT%{_bindir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README TODO Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
#%{_applnkdir}/DockApplets/wmrecord.desktop
