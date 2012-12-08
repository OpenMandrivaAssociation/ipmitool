Summary:	Utility for interfacing with IPMI devices
Name:		ipmitool
Version:	1.8.11
Release:	11
License:	GPL
Group:		System/Kernel and hardware
URL:		http://ipmitool.sourceforge.net/
Source0:	http://optusnet.dl.sourceforge.net/sourceforge/ipmitool/%{name}-%{version}.tar.gz
Patch0:		ipmitool-1.8.10-fix-format-error.patch
Patch1:		ipmitool-1.8.11-CVE-2011-4339.diff
Requires:	freeipmi
BuildRequires:	freeipmi-devel
BuildRequires:	pkgconfig(openssl)
ExcludeArch:	%arm %mips

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
%patch0 -p 1
%patch1 -p0 -b .CVE-2011-4339

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
%makeinstall_std

rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_datadir}/ipmitool


%changelog
* Thu Jan 12 2012 Oden Eriksson <oeriksson@mandriva.com> 1.8.11-9
+ Revision: 760488
- sync with MDVSA-2011:196

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.11-8
+ Revision: 665516
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.11-7mdv2011.0
+ Revision: 605979
- rebuild

* Fri Apr 09 2010 Funda Wang <fwang@mandriva.org> 1.8.11-6mdv2010.1
+ Revision: 533318
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.11-5mdv2010.1
+ Revision: 511577
- rebuilt against openssl-0.9.8m

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 1.8.11-4mdv2010.1
+ Revision: 475302
- rebuild for new freeipmi

* Fri Sep 25 2009 Olivier Blin <blino@mandriva.org> 1.8.11-3mdv2010.0
+ Revision: 449105
- do not build on mips & arm (from Arnaud Patard)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.8.11-2mdv2010.0
+ Revision: 425369
- rebuild

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.11-1mdv2009.1
+ Revision: 350614
- update to new version 1.8.11

* Thu Jan 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.10-1mdv2009.1
+ Revision: 327106
- new version
- fix format error

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.8.9-4mdv2009.0
+ Revision: 221635
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.8.9-3mdv2008.1
+ Revision: 127108
- kill re-definition of %%buildroot on Pixel's request

  + Erwan Velu <erwan@mandriva.org>
    - Fixing buildrequires for lanplus (#32117)


* Thu Mar 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.9-2mdv2007.1
+ Revision: 144249
- freeipmi-devel is a build dependency

* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.9-1mdv2007.1
+ Revision: 143715
- new version

* Wed Jan 17 2007 Erwan Velu <erwan@mandriva.org> 1.8.8-1mdv2007.1
+ Revision: 109930
- 1.8.8
- Import ipmitool

* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.8.7-2mdv2007.0
- Rebuild

* Fri Mar 31 2006 Erwan Velu <erwan@seanodes.com> 1.8.7-1mdk
- 1.8.7

* Thu Jan 19 2006 Erwan Velu <erwan@seanodes.com> 1.8.6-1mdk
- 1.8.6

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.8.2-2mdk
- rebuilt against openssl-0.9.8a

* Tue Jun 07 2005 Erwan Velu <velu@seanodes.com> 1.8.2-1mdk
- 1.8.2
- Adding ipmievd

* Sat Apr 02 2005 Olivier Blin <oblin@mandrakesoft.com> 1.6.0-2mdk
- don't require libs in main package, they aren't produced anymore

* Thu Mar 03 2005 Erwan Velu <erwan@seanodes.com> 1.6.0-1mdk
- 1.6.0

* Thu Aug 19 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.5.9-5mdk
- lib64 fixes

* Sat Aug 14 2004 Erwan Velu <erwan@mandrakesoft.com> 1.5.9-4mdk
- Fixing description

* Thu Aug 12 2004 Erwan Velu <erwan@mandrakesoft.com> 1.5.9-3mdk
- Requires IPMI

* Fri Jul 16 2004 Erwan Velu <erwan@mandrakesoft.com> 1.5.9-2mdk
- Fixing versionning of libs
- Fixing requires

* Fri Jul 16 2004 Erwan Velu <erwan@mandrakesoft.com> 1.5.9-1mdk
- Initial MDK Release

