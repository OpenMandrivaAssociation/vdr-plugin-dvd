
%define plugin	dvd
%define name	vdr-plugin-%plugin
%define version	0.3.6
%define betaver	b03
%define cvsrev	20060506
%define rel	10
%define release	0.%betaver.%cvsrev.%rel

Summary:	VDR plugin: turn VDR into an (almost) full featured DVD player
Name:		%name
Version:	%version
Release:	%mkrel %release
Group:		Video
License:	GPL
URL:		http://sourceforge.net/projects/dvdplugin
Source:		vdr-%{plugin}-%{cvsrev}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	libdvdnav-devel liba52dec-devel
Requires:	vdr-abi = %vdr_abi
Requires(post):	vdr-common

%description
This is the DVD plugin for the Video Disk Recorder (VDR).

%prep
%setup -q -n %{plugin}
# script-without-shellbang
chmod -x README COPYING HISTORY CONTRIBUTORS

%vdr_plugin_params_begin %plugin
# DVD device
# default: /dev/dvd
var=DVD_DEVICE
param=--dvd=DVD_DEVICE
%vdr_plugin_params_end

%build
%vdr_plugin_build

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


