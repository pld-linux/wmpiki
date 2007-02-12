Summary:	Hosts activity checker
Summary(pl.UTF-8):	Monitor aktywności hostów
Name:		wmpiki
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://clay.ll.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	119c87de9c0f2aa2e496a9797b1e9055
Source1:	%{name}.desktop
Patch0:		%{name}-home_etc.patch
URL:		http://clay.ll.pl/dockapps.html
BuildRequires:	XFree86-devel
Requires:	iputils-ping
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmpiki is a dockapp which checks and displays small leds for indicate
hosts activity (up to eight hosts).

%description -l pl.UTF-8
Wmpiki jest apletem, który sprawdza i przy pomocy małych diod wskazuje
aktywność hostów w sieci (do ośmiu hostów).

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall" \
	LIBS="-L/usr/X11R6/%{_lib} -lXpm -lXext -lX11"

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
