# Ansible first test

// Initialization stuff.
systemctl start docker
cat /dev/null > ~/.ssh/known_hosts

// Running servers (containers)
docker run -d -p 2221:22 --name pythonssh1 davidlor/python-ssh
    ssh pythonssh@172.17.0.2 -p 22 // pass: sshpass

// Ansible CLI
ansible mynodes -m ping
ansible all -m ping
ansible all -m shell -a "uname -a"

// Playbooks
ansible-playbook ping-playbook.yml

// Modules
ansible-doc -l // to see the list of available modules.
ansible-doc <module_name>
