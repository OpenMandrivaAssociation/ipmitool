%define uversion %(echo %{version} | sed -e 's,\\.,_,g')

Summary:	Utility for interfacing with IPMI devices
Name:		ipmitool
Version:	1.8.19
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://github.com/ipmitool/ipmitool
Source0:	https://github.com/ipmitool/ipmitool/archive/refs/tags/IPMITOOL_%{uversion}.tar.gz

BuildRequires:	pkgconfig(libfreeipmi)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	readline-devel
Requires:	freeipmi

%description
IPMI stands for Intelligent Platform Management Interface 
and is an open standard for machine health, and (remote) control
and is implemented by many hardware vendors - Intel is one of the originators, 
and early adopters of the standard.
This package contains a utility for interfacing with IPMI-enabled devices
through either the OpenIPMI kernel driver or with IPMI-over-LAN protocol.
These functions include printing FRU(Field Replaceable Unit) information,
LAN configuration, sensor readings, and remote chassis power control. 

%prep
%autosetup -p1 -n %{name}-IPMITOOL_%{uversion}
./bootstrap

%conf
%configure \
	--enable-ipmievd \
	--enable-intf-lan \
	--enable-intf-open \
	--enable-intf-lanplus \
	--with-kerneldir=/usr/src/linux \
	--with-plugin-path=%{_libdir}/ipmitool

%build
%make_build

%install
%make_install

rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_datadir}/ipmitool
