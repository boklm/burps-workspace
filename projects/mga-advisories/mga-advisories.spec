[%- PROCESS pkg_rel.spec -%]
Name:           [% project %]
Version:        [% c('version') %]
Release:        [% d.rel_macro %] [% rel %]
Source:         %{name}-%{version}.tar.[% c('compress_tar') %]
Summary:        [% p.summary %]
URL:            [% p.url %]
License:        CC0
Group:          Text tools
BuildArch:      noarch
Requires:       perl(Template::Plugin::JSON)
%description
[% p.description -%]

%prep
%setup -q

%build

%install
%makeinstall_std perldir=%{perl_vendorlib}

%files
%doc README COPYING NEWS
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/mgaadv
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config
%{_datadir}/%{name}/tmpl
%{_datadir}/%{name}/static
%{perl_vendorlib}/MGA/Advisories.pm
