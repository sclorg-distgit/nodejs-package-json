%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name package-json

Summary:       Get the package.json of a package from the npm registry
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.3.0
Release:       5%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/package-json
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Get the package.json of a package from the npm registry.

%prep
%setup -q -n package

%nodejs_fixdep semver 5.x

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Feb 24 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.0-5
- Fix dependency

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.0-3
- Rebuilt with updated metapackage

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 2.3.0-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.3.0-1
- Initial package
