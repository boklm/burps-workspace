[% PROCESS pkg_rel.spec -%]
Name:           mgagit
Version:        [% c('version') %]
Release:        [% d.rel_macro %] [% rel %]
Source:         %{name}-%{version}.tar.xz
Summary:        Tool to generate Mageia advisories pages and emails
URL:            http://gitweb.mageia.org/software/infrastructure/mgagit/about/
License:        CC0
Group:          Text tools
BuildArch:      noarch
%description
Tool to manage Mageia git repositories.

%prep
%setup -q

%build

%install
%makeinstall_std perldir=%{perl_vendorlib}

%files
%doc README COPYING NEWS
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config
%{_datadir}/%{name}/tmpl
%{perl_vendorlib}/MGA/Git.pm
