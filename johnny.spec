Summary:	GUI for John the Ripper
Name:		johnny
Version:	2.2
Release:	1
License:	BSD
Group:		Monitoring
Url:		https://www.openwall.com/john/johnny
Source0:	https://github.com/openwall/johnny/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)

Requires:	john

%description
Johnny the open source cross-platform GUI frontend for John the Ripper, the
popular password cracker, written in C++ using the Qt framework.

Johnny's aim is to automate and simplify the password cracking routine on the
Desktop as well as add extra functionality like session management and easy
hash/password management, on top of the immense capabilities and features
offered by John the Ripper.

The application uses John The Ripper for the actual work, thus it needs to be
installed on your system. Official core (proper) version and the
community-enhanced version (jumbo) are both supported. The latter exposes more
functionality like extra cracking modes and hash types support.

%files
%license LICENSE
%doc CHANGELOG README
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}*.xpm	
%{_iconsdir}/hicolor/*/apps/%{name}*.png

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%qmake_qt5
%make_build

%install
# NOTE: make install has any effects
#make_install

# binary
install -dm 0755 %{buildroot}%{_bindir}/
install -pm 0755 %{name} %{buildroot}%{_bindir}/

# icons
#    app
for i in 16 22 32 48 64 128 256 512
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/
	convert -scale ${i}x${i} resources/icons/%{name}_128.png \
			%{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}.png
done
#    pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -scale ${i}x${i} resources/icons/%{name}_128.png \
		%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# .desktop
install -dm 0755 %{buildroot}%{_datadir}/applications/
install -dm 0755 %{buildroot}%{_datadir}/applications/
cat >%{buildroot}%{_datadir}/applications/%{vendor}-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Johnny
GenericName=Johnny
Comment=A GUI for John the Ripper
Exec=/usr/bin/johnny
Icon=/usr/share/pixmaps/johnny.png
StartupNotify=true
Terminal=false
Type=Application
Categories=Application;System
EOF

