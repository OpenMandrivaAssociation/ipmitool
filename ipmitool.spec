%define	name	ipmitool
%define	version	1.8.11
%define release	%mkrel 7
%define	lib_major	1
%define	lib_name	%mklibname %{name} %{lib_major}

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Utility for interfacing with IPMI devices
Source0:	    http://optusnet.dl.sourceforge.net/sourceforge/ipmitool/%{name}-%{version}.tar.gz
Patch:          ipmitool-1.8.10-fix-format-error.patch
License:	    GPL
Group:		    System/Kernel and hardware
Url:		    http://ipmitool.sourceforge.net/ 
Requires:	    IPMI
BuildRequires:	    freeipmi-devel, openssl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}
ExcludeArch:	    %arm %mips

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
%setup -q
%patch -p 1

%build
%configure2_5x \
    --enable-ipmievd \
    --enable-intf-lan \
    --enable-intf-open \
    --enable-intf-lanplus \
    --with-kerneldir=/usr/src/linux \
    --with-plugin-path=%{_libdir}/ipmitool
make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_datadir}/ipmitool


