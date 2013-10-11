Name:           [% project %]
Version:        [% c('version') %]
Release:        [% d.rel_macro %] [% c('rpm_rel') %]
Source:         %{name}-%{version}.tar.[% c('compress_tar') %]
Summary:        [% c('summary') %]
URL:            [% c('url') %]
License:        CC0
Group:          Text tools
BuildRequires:  asciidoc
BuildArch:      noarch
%description
[% c('description') -%]

%prep
%setup -q

%build

%install
%makeinstall_std perldir=%{perl_vendorlib}

%files
%doc README.md COPYING
%{_bindir}/%{name}
%{perl_vendorlib}/MkPkg.pm
