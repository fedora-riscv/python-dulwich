%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname dulwich

%filter_provides_in %{python_sitearch}
%filter_setup

Name:           python-%{srcname}
Version:        0.8.0
Release:        1%{?dist}
Summary:        A python implementation of the Git file formats and protocols

Group:          Development/Libraries
License:        GPLv2+
URL:            http://samba.org/~jelmer/dulwich/
Source0:        http://samba.org/~jelmer/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose


%description
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.


%prep
%setup -q -n %{srcname}-%{version}


%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%check
cd dulwich/tests
#nosetests test*.py
nosetests test_blackbox.py
nosetests test_client.py
#nosetests test_diff_tree.py
nosetests test_fastexport.py
nosetests test_file.py
nosetests test_index.py
nosetests test_lru_cache.py
nosetests test_objects.py
nosetests test_object_store.py
nosetests test_patch.py
nosetests test_pack.py
nosetests test_protocol.py
nosetests test_repository.py
nosetests test_server.py
nosetests test_web.py


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING HACKING NEWS README docs/
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%{python_sitearch}/%{srcname}*
%exclude %{python_sitearch}/%{srcname}/tests*


%changelog
* Thu Oct 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Updated to new upstream version 0.8.0

* Sun Apr 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Updated to new upstream version 0.7.1

* Fri Mar 11 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-3
- Test section reworked

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Updated to new upstream version 0.7.0

* Sat Nov 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Filtering added
- Updated to new upstream version 0.6.2

* Wed Sep 01 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Fixed grep parameter
- Run all test now
- Updated to new upstream version 0.6.1

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-3
- Removed exec permission from test.py
- Added python-nose

* Fri Jun 25 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-2
- Changed summary
- Change to srcname
- Fixed rpmlint issue
- Added check section and exclude the tests directory

* Thu Jun 17 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Fixed some rpmlint issues
- Added docs directory
- Updated to new upstream version 0.6.0

* Wed Apr 28 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Doc added
- Added BR setuptools

* Fri Apr 16 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> 0.5.0-1
- Initial package
