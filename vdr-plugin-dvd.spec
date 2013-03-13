
%define plugin	dvd
%define betaver	b03
%define cvsrev	20071030
%define rel	8
%define release	0.%betaver.%cvsrev.%rel

Summary:	VDR plugin: turn VDR into an (almost) full featured DVD player
Name:		vdr-plugin-%plugin
Version:	0.3.6
Release:	%release
Group:		Video
License:	GPL
URL:		http://sourceforge.net/projects/dvdplugin
Source:		vdr-%{plugin}-%{cvsrev}.tar.bz2
Patch0:		dvd-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0-7
BuildRequires:	libdvdnav-devel liba52dec-devel
Requires:	vdr-abi = %vdr_abi
Requires(post):	vdr-common

%description
This is the DVD plugin for the Video Disk Recorder (VDR).

%prep
%setup -q -n %{plugin}
%patch0 -p1
%vdr_plugin_prep
# script-without-shellbang
chmod -x README COPYING HISTORY CONTRIBUTORS

%vdr_plugin_params_begin %plugin
# DVD device
# default: /dev/dvd
var=DVD_DEVICE
param=--dvd=DVD_DEVICE
%vdr_plugin_params_end

%build
VDR_PLUGIN_EXTRA_FLAGS=
%if %{mdkversion} >= 200900
# mdv #40406
mkdir -p dvdnav
sed 's,\*this,*cthis,' %{_includedir}/dvdnav/dvdnav.h > dvdnav/dvdnav.h
diff -u %{_includedir}/dvdnav/dvdnav.h dvdnav/dvdnav.h || :
VDR_PLUGIN_EXTRA_FLAGS="-I$PWD"
%endif
# mdv #35140
VDR_PLUGIN_EXTRA_FLAGS="$VDR_PLUGIN_EXTRA_FLAGS -D__STDC_LIMIT_MACROS"
%vdr_plugin_build LDFLAGS="%vdr_plugin_ldflags"

%install
%vdr_plugin_install

%post
%{_bindir}/gpasswd -a vdr cdrom >/dev/null
%{_bindir}/gpasswd -a vdr cdwriter >/dev/null

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY CONTRIBUTORS




%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.7mdv2011.0
+ Revision: 404574
+ rebuild (emptylog)

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.6mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- adapt for vdr compilation flags handling changes, bump buildrequires

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.5mdv2009.1
+ Revision: 359307
- rebuild for new vdr

* Sun Sep 07 2008 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.4mdv2009.0
+ Revision: 282079
- rebuild due to missing package on x86_64

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.3mdv2009.0
+ Revision: 197886
- add a workaround for dvdnav bug #40406 causing build failure
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.2mdv2008.1
+ Revision: 145093
- adapt for VDR_PLUGIN_FLAGS
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20071030.1mdv2008.1
+ Revision: 103843
- add -D__STDC_LIMIT_MACROS into flags to fix build with recent
  libdvdnav (see #35140)
- new snapshot
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20070501.4mdv2008.0
+ Revision: 49990
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20070501.3mdv2008.0
+ Revision: 42076
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20070501.2mdv2008.0
+ Revision: 22739
- rebuild for new vdr

* Tue May 01 2007 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20070501.1mdv2008.0
+ Revision: 20065
- new snapshot


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.10mdv2007.0
+ Revision: 90911
- rebuild for new vdr
- add vdr user to cdwriter group

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.9mdv2007.1
+ Revision: 73983
- rebuild for new vdr
- Import vdr-plugin-dvd

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.8mdv2007.0
- rebuild for new vdr

* Fri Sep 01 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.7mdv2007.0
- add vdr to cdrom group

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.2mdv2007.0
- rebuild for new vdr

* Fri Jun 02 2006 Anssi Hannula <anssi@mandriva.org> 0.3.6-0.b03.20060506.1mdv2007.0
- initial Mandriva release

