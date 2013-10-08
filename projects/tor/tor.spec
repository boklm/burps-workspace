%define runuser toruser
%define _tmpfilesdir /usr/lib/tmpfiles.d
%define _tmpfilescreate() echo %{1}


Name:		tor
Version:	[% c('version') %]
Release:	[% d.rel_macro %] [% c('rpm_rel') %]
Summary:	Anonymizing overlay network for TCP (The onion router)
URL:		http://www.torproject.org/
Group:		Networking/Other
License:	BSD-like
Requires(post):  systemd >= %{systemd_required_version}
Requires(post):  rpm-helper >= 0.24.8-1
Requires(preun): rpm-helper >= 0.24.8-1
Requires(post):   sysvinit
Requires(preun):  sysvinit
Requires(postun): sysvinit
Requires:	openssl >= 0.9.6
Requires:	tsocks
BuildRequires:	openssl-devel >= 0.9.6 
BuildRequires:	libevent-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf2.5
BuildRequires:	transfig, texlive
BuildRequires:	ghostscript
BuildRequires:  asciidoc
Source0:	%{name}-%{version}.tar.xz
Source1:	%{name}.logrotate
Source2:	%{name}.init
Source3: 	%{name}.sysconfig
Source4:	%{name}.service
Source5:	%{name}-tmpfiles.conf

%description
Tor is a connection-based low-latency anonymous communication system.

This package provides the "tor" program, which serves as both a client and
a relay node. Scripts will automatically create a "%{runuser}" user and
group, and set tor up to run as a daemon when the system is rebooted.

Applications connect to the local Tor proxy using the SOCKS
protocol. The local proxy chooses a path through a set of relays, in
which each relay knows its predecessor and successor, but no
others. Traffic flowing down the circuit is unwrapped by a symmetric
key at each relay, which reveals the downstream relay.

%prep
%setup -q
 
%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall

%define _logdir %{_var}/log

mkdir -p ${RPM_BUILD_ROOT}%{_initrddir}
cat %{SOURCE2} > ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
chmod 0755 ${RPM_BUILD_ROOT}%{_initrddir}/%{name}

install -p -m 644 ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/torrc.sample ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/torrc

mkdir -p -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
cat %{SOURCE1} > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/
cat %{SOURCE3} > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

mkdir -p -m 700 ${RPM_BUILD_ROOT}%{_localstatedir}/lib/%{name}
mkdir -p -m 755 ${RPM_BUILD_ROOT}%{_var}/%{name}
mkdir -p -m 755 ${RPM_BUILD_ROOT}%{_logdir}/%{name}

# Bash completion
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/bash_completion.d
echo 'complete -F _command $filenames torify' > ${RPM_BUILD_ROOT}%{_sysconfdir}/bash_completion.d/%{name}

# Systemd support
install -D -p -m 0644 %SOURCE4 $RPM_BUILD_ROOT%_unitdir/%name.service
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%pre
%_pre_useradd %{runuser} / /bin/false

%post
%_tmpfilescreate %{name}
%_post_service %{name}

%preun
%_preun_service %{name}
rm -f %{_localstatedir}/%{name}/cached-directory
rm -f %{_localstatedir}/%{name}/bw_accounting
rm -f %{_localstatedir}/%{name}/control_auth_cookie
rm -f %{_localstatedir}/%{name}/router.desc
rm -f %{_localstatedir}/%{name}/fingerprint

%postun
%_postun_userdel %{runuser}
%_postun_groupdel %{runuser}

%files
%doc ReleaseNotes INSTALL LICENSE README ChangeLog doc/HACKING
%{_mandir}/man*/*
%{_bindir}/tor
%{_bindir}/torify
%{_bindir}/tor-resolve
%{_bindir}/tor-gencert
%config(noreplace) %attr(0755,%{runuser},%{runuser}) %{_initrddir}/%{name}
%_unitdir/%name.service
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755,root,%{runuser}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0644,root,%{runuser}) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0700,%{runuser},%{runuser}) %dir %{_localstatedir}/lib/%{name}
%attr(0750,%{runuser},%{runuser}) %dir %{_var}/%{name}
%attr(0750,%{runuser},%{runuser}) %dir %{_logdir}/%{name}
%{_sysconfdir}/bash_completion.d/%{name}
%{_datadir}/%{name}
