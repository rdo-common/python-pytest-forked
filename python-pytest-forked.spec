%global pypi_name pytest-forked
%global desc The pytest-forked plugin extends py.test by adding an option to run tests in\
isolated forked subprocesses. This is useful if you have tests involving C or\
C++ libraries that might crash the process. To use the plugin, simply use the\
--forked argument when invoking py.test.

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        py.test plugin for running tests in isolated forked subprocesses

License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel python3-devel
BuildRequires:  python2-py python2-pytest python2-setuptools_scm
BuildRequires:  python3-py python3-pytest python3-setuptools_scm

%description
%{desc}

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-py python2-pytest
%description -n python2-%{pypi_name}
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-py python3-pytest
%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -f testing/conftest.pyc
rm -rf testing/__pycache__

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} testing
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} testing


%files -n python2-%{pypi_name}
%doc example/boxed.txt README.rst
%license LICENSE
%{python2_sitelib}/pytest_forked*

%files -n python3-%{pypi_name}
%doc example/boxed.txt README.rst
%license LICENSE
%{python3_sitelib}/pytest_forked*

%changelog
* Wed Feb 20 2019 Scott Talbert <swt@techie.net> - 1.0.2-1
- New upstream release 1.0.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Scott Talbert <swt@techie.net> - 1.0.1-1
- New upstream release 1.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Scott Talbert <swt@techie.net> - 0.2-2
- Updated to use py[23]dist macros for BR and R

* Thu Aug 10 2017 Scott Talbert <swt@techie.net> - 0.2-1
- Initial package.
