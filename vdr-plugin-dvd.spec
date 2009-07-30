
%define plugin	dvd
%define name	vdr-plugin-%plugin
%define version	0.3.6
%define betaver	b03
%define cvsrev	20071030
%define rel	7
%define release	0.%betaver.%cvsrev.%rel

Summary:	VDR plugin: turn VDR into an (almost) full featured DVD player
Name:		%name
Version:	%version
Release:	%mkrel %release
Group:		Video
License:	GPL
URL:		http://sourceforge.net/projects/dvdplugin
Source:		vdr-%{plugin}-%{cvsrev}.tar.bz2
Patch0:		dvd-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%{_bindir}/gpasswd -a vdr cdrom >/dev/null
%{_bindir}/gpasswd -a vdr cdwriter >/dev/null
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY CONTRIBUTORS


