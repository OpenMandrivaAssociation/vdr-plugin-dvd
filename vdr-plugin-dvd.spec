%define plugin	dvd
%define betaver	b03
%define cvsrev	20090118

Summary:	VDR plugin: turn VDR into an (almost) full featured DVD player
Name:		vdr-plugin-%plugin
Version:	0.3.6
Release:	0.%betaver.%cvsrev.2
Group:		Video
# GPLv2+ due to dvdspu.c, otherwise would be GPL+
License:	GPLv2+
URL:		http://sourceforge.net/projects/dvdplugin
Source:		vdr-%{plugin}-%{cvsrev}.tar.bz2
# from e-tobi debian repository:
Patch0:		11_allow-non-existing-dvd-drive.dpatch
Patch1:		12_dvd-fixed-german-spelling.dpatch
BuildRequires:	vdr-devel >= 1.6.0-7
BuildRequires:	libdvdnav-devel 
BuildRequires:	a52dec-devel
Requires:	vdr-abi = %vdr_abi
Requires(post):	vdr-common

%description
This is the DVD plugin for the Video Disk Recorder (VDR).

%prep
%setup -q -n %{plugin}
%autopatch -p1
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
%vdr_plugin_build LDFLAGS="%vdr_plugin_ldflags"

%install
%vdr_plugin_install

%post
%{_bindir}/gpasswd -a vdr cdrom >/dev/null
%{_bindir}/gpasswd -a vdr cdwriter >/dev/null

%files -f %plugin.vdr
%doc README COPYING HISTORY CONTRIBUTORS






