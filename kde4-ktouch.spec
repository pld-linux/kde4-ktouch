%define		_state		stable
%define		orgname		ktouch

Summary:	K Desktop Environment - Program for learning touch typing
Summary(pl_PL.UTF8):	K Desktop Environment - Program do nauki maszynopisania
Name:		kde4-ktouch
Version:	4.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	9a691e993c46253d2a087c15d0404c76
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdeedu-ktouch < 4.6.99
Obsoletes:	ktouch <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTouch is a program for learning to touch type. It provides you with
text to train on, and adjust to different levels, depending on how
good you are. It can display which key to press next, and the correct
finger to use. It's the perfect touch typing tutor, you learn typing
with all the fingers without looking at the keys, in an step by step
way. It is convenient for all ages, and the perfect typing tutor for
schools, universities and individuals.

%description -l pl.UTF-8
KTouch to program do nauki maszynopisania. Dostarcza tekst do ćwiczeń,
dostosowany do różnych poziomów, zależnie od stopnia zaawansowania.
Może wyświetlać, który klawisz trzeba nacisnąć, i którego palca należy
użyć. Jest świetnym programem do nauki maszynopisania, uczy pisać
wszystkimi palcami bez patrzenia na klawisze, krok po kroku. Jest
wygodny w każdym wieku, jest świetny dla szkół, uniwersytetów i
jednostek.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%{_datadir}/apps/ktouch
%{_desktopdir}/kde4/ktouch.desktop
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/config.kcfg/ktouch.kcfg
%{_iconsdir}/hicolor/*x*/apps/ktouch.png
%{_iconsdir}/hicolor/scalable/apps/ktouch.svgz
%{_mandir}/man1/ktouch.1*
