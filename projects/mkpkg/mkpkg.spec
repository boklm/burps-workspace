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
[% IF c('timestamp') >= 1381244225 -%]
%{perl_vendorlib}/MkPkg/DefaultConfig.pm
[% END -%]
[% IF c('timestamp') >= 1381356133 -%]
%{_mandir}/man1/mkpkg.1*
%{_mandir}/man1/mkpkg-*.1*
%{_mandir}/man7/mkpkg_*.7*
[% END -%]
