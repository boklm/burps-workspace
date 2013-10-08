Name:           [% project %]
Version:        [% c('version') %]
Release:        [% d.rel_macro %] [% c('rpm_rel') %]
Source:         %{name}-%{version}.tar.[% c('compress_tar') %]
Summary:        [% c('summary') %]
URL:            [% c('url') %]
License:        CC0
Group:          Text tools
BuildArch:      noarch
Requires:       perl(Template::Plugin::JSON)
%description
[% c('description') -%]

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
