# Puppet Stages
stage {
    'users':          before => Stage['folders'];
    'folders':        before => Stage['nodejs'];
    'nodejs':         before => Stage['repos'];
    'repos':          before => Stage['updates'];
    'updates':        before => Stage['packages'];
    'packages':       before => Stage['pipackages'];
    'pipackages':     before => Stage['geminstall'];
    'geminstall':     before => Stage['supervisor'];
    'supervisor':     before => Stage['postgres_role'];
    'postgres_role':  before => Stage['postgres_db'];
    'postgres_db':    before => Stage['services'];
    'services':       before => Stage['main'];
}

class users {
    group { "www-data":
        ensure => "present",
     }
}

class folders {
    file { ['/', '/web']:
        ensure => 'directory',
        owner => 'www-data',
        group => 'www-data',
        mode => 0755
    }
}

class nodejs {
    exec {
        "node-backports":
            command => '/bin/echo "deb http://ftp.us.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list',
            timeout => 0
    }
}

class repos {
}

class updates {
    exec { "aptitude-update":
        command => "/usr/bin/aptitude update -y -q",
        timeout => 0
    }
}

class packages {
    package {[
            "python",
            "python-dev",
            "python-pip",
            "postgresql",
            "postgresql-contrib",
            "libffi-dev",
            "libpq-dev",
            "nodejs",
            "node-coffeescript"]:            
        ensure => "present",
    }
}

class geminstall {
    exec {
        "sass":
            command => '/usr/bin/sudo gem install sass',
            timeout => 0,
            cwd => '/web';
    }
}

class pipackages {
    exec {
        "requirements":
            command => '/usr/bin/pip install -r requirements.txt',
            cwd => '/web';
    }
}

class supervisor {
    exec {
        "supervisord":
            command => '/usr/bin/sudo pip install supervisor',
            cwd => '/web';

        "supervisord-conf":
            command => '/usr/bin/sudo cp /web/manifests/supervisord.conf /etc/supervisord.conf',
            unless => '/bin/ls /etc/supervisord.conf';

        "supervisord-initscript":
            command => '/usr/bin/sudo cp /web/manifests/supervisord /etc/init.d/supervisord',
            unless => '/bin/ls /etc/init.d/supervisord';

        "supervisord-udev":
            command => '/usr/bin/sudo cp /web/manifests/50-vagrant-mount.rules /etc/udev/rules.d/50-vagrant-mount.rules',
            unless => '/bin/ls /etc/rules.d/50-vagrant-mount.rules';
    }
}

class postgres_role {
    exec {
        "postgres-test-user":
            command => '/usr/bin/sudo -u postgres psql -c "CREATE USER postgres_test_user WITH SUPERUSER LOGIN PASSWORD \'pg_tst_pw\';"',
            cwd => '/web',
            unless => '/usr/bin/sudo -u postgres psql -c "SELECT rolname FROM pg_roles WHERE rolname = \'postgres_test_user\';" | grep postgres_test_user';
    }
}

class postgres_db {
    exec { 
        "postgres-test-db":
            command => '/usr/bin/sudo -u postgres psql -c "CREATE DATABASE postgres_test_db OWNER postgres_test_user;"',
            cwd => '/web',
            unless => '/usr/bin/sudo -u postgres psql -c "SELECT datname FROM pg_database WHERE datname = \'postgres_test_db\';" | grep postgres_test_db',
            require => Exec['postgres-test-user'];
    }
}

class services {
    exec {
        "web":
            command => '/etc/init.d/supervisord start',
            cwd => '/web';
    }
}

class {
    users:          stage => "users";
    repos:          stage => "repos";
    updates:        stage => "updates";
    nodejs:         stage => "nodejs";
    pipackages:     stage => "pipackages";
    packages:       stage => "packages";
    geminstall:     stage => "geminstall";
    supervisor:     stage => "supervisor";
    postgres_role:  stage => "postgres_role";
    postgres_db:    stage => "postgres_db";
    services:       stage => "services";
}
