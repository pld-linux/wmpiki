Summary:	Hosts activity checker
Summary(pl):	Monitor aktywno¶ci hostów
Name:		wmpiki
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://clay.ll.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	f76d66a4856746e65a2607b7325d1cf0
Source1:	%{name}.desktop
URL:		http://clay.ll.pl/dockapps.html
BuildRequires:	XFree86-devel
Requires:	iputils-ping	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmpiki is a dockapp which checks and displays small leds for indicate
hosts activity (up to eight hosts).

%description -l pl
Wmpiki jest apletem, który sprawdza i przy pomocy ma³ych diod wskazuje
aktywno¶æ hostów w sieci (do o¶miu hostów).

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README config.example
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
