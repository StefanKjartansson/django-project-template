VROOT = '/home/vagrant'
PROJECT_NAME = File.expand_path(File.dirname(__FILE__)).split('/')[-1]

Vagrant::Config.run do |config|

  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.network :hostonly, "33.33.33.10"
  config.vm.forward_port 8000, 8000
  config.ssh.forward_agent = true 
  
  config.vm.share_folder(PROJECT_NAME, "#{VROOT}/#{PROJECT_NAME}", 
    ".", :nfs => true)

  config.vm.provision :shell do |shell|
    shell.inline = <<-eos
        #!/bin/sh
        sed -i "s/us.archive.ubuntu.com/ftp.rhnet.is/g" /etc/apt/sources.list
        apt-get update -y
        apt-get install -y build-essential openssh-server curl vim git language-pack-is python-setuptools python-dev libevent-dev redis-server
        apt-get install -y nodejs npm
        npm install less coffee-script -g
        grep -q github .ssh/known_hosts 2>/dev/null || ssh-keyscan -t rsa github.com > .ssh/known_hosts
        easy_install pip
        pip install -U distribute pip virtualenv
        test -d #{VROOT}/virtualenvs || su vagrant -c "mkdir #{VROOT}/virtualenvs"
        test -d #{VROOT}/virtualenvs/#{PROJECT_NAME} || su vagrant -c "virtualenv #{VROOT}/virtualenvs/#{PROJECT_NAME}"
    eos
  end
end
