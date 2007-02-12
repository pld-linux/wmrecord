Summary:	A Dockable General Purpose Recording Utility
Summary(pl.UTF-8):	Dokowalne Narzędzie do Nagrywania
Name:		wmrecord
Version:	1.0.5.3
Release:	1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://www.matracas.net/other_software/wmrecord/%{name}-1.0.5_20040218_0029.tgz
# Source0-md5:	60a87268cd4de9486df934fb42ac3b71
Source1:	%{name}.desktop
URL:		http://www.matracas.net/other_software/wmrecord/index.en.html
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMRecord is a general purpose audio recording utility for X11,
currently using the Open Sound System (OSS). The interface is designed
to work in conjunction with WindowMaker's Dock or AfterStep's Wharf,
two popular window managers for the X Window System.

%description -l pl.UTF-8
WMRecord jest narzędziem nagrywającym dla środowiska X11, w obecnej
chwili wykorzystującym sterowniki Open Sound System (OSS). Interfejs
programu jest zaprojektowany do pracy w połączeniu z Dokiem
WindowMakera lub AfterStepa.

%prep
%setup -q -n %{name}-1.0.5

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LIBDIR=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install man/wmrecord.1 $RPM_BUILD_ROOT%{_mandir}/man1
install wmrecord $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/wmrecord
%{_mandir}/man1/wmrecord.1*
%{_desktopdir}/docklets/wmrecord.desktop
