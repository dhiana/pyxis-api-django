# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define :pyxis_api do |api_config|
    api_config.vm.box = 'ubuntu/trusty64'
    api_config.vm.network :private_network, ip: '192.168.33.43'

    api_config.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'api_servers.yml'
      ansible.limit = 'api-node'
      ansible.sudo = true
      ansible.inventory_path = 'hosts'
      ansible.extra_vars = {
        ansible_ssh_user: 'vagrant'
      }
    end

    api_config.vm.provider 'virtualbox' do |v|
      v.memory = 1048
    end
  end
end
