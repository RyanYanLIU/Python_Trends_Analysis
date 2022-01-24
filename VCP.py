#!/usr/bin/python
'''VCP考试练习'''
import random
import os
import subprocess
topic = {'''An administrator is installing a Platform Services Controller instance.
Which two options are available during the installation process? (Choose two.)
A. choose deployment size
B. specify vSphere administrator credentials
C. enable Enhanced Linked Mode
D. create a vCenter Single sign-on domain
E. join an existing domain''':'DE',
            '''A vSphere Administrator has multiple virtual machines running on a VMFS datastore.
Which option prioritizes the disk access for the virtual machines?
A. Disk Shares
B. Disk Mode
C. Disk Type
D. Hard Disk''':'A',
            '''What should be installed on a VM to assist with VM-to-host time synchronization?
A. VMware Tools
B. vRA guest agent
C. vROps agent
D. Guest Operations Manager''':'A',
            '''An administrator runs a vSphere cluster containing database VMs with extremely heavy disk I/O.
Database VMs are placed on a costly all-flash array. The workloads are not memory intensive.
How can the administrator ensure the most cost-effective utilization of the all-flash storage array?
A. Enable Storage I/O Control on the flash datastores.
B. Install VMware Tools on the database VMs to ensure the hypervisor can receive I/O metrics.
C. Use a VM-to-Host affinity rule to ensure database VMs are prioritized.
D. Edit the cluster settings to place the virtual machine swap file on a different storage tier.''':'D',
            '''An administrator has an environment with these conditions and requirements:
How can the administrator meet the conditions and requirements?
A. Adjust NIOC or SIOC as appropriate to give the QA department a higher compute priority within the
cluster.
B. Create a resource pool for each department and use the Shares attribute to prioritize the allocation of
resources.
C. Assign affinity or anti-affinity rules to the appropriate VMs for each department.
D. Set the VM priority to high for QA department VMs and normal for Marketing department VMs.''':'B',
            '''What is a benefit of using resource pools?
            A. Increased visibility of user activity
B. Increased vMotion efficiency for a set of VMs
C. Increased accuracy for proactive resources for a set of VMs
D. Increased ease of reserving resources for a set of VMs''':'D',
            '''This error is generated when a vSphere administrator takes a VM snapshot:
An error occurred while taking a snapshot: Failed to quiesce the virtual machine
What should the administrator investigate to determine the cause of the failure?
A. Check if the virtual machine is already running on snapshots.
B. Check if the virtual machine is in suspended state.
C. Check if VMware Tools is installed on virtual machine.
D. Check if the virtual machine has an ISO mounted.''':'C',
            '''A vSphere administrator is working in a high security environment. The administrator wants to ensure
unencrypted VMs can be migrated securely.
What should the vSphere administrator use to meet this requirement?
A. vTPM
B. UEFI Secure Boot
C. KMS server
D. encrypted vSphere vMotion''':'D',
            '''For security reasons the VMware vSphere Update Manager (VUM) has no Internet access.
What can be used to provide a central shared repository in a DMZ?
A. VMware vSphere Update Manager Download Service
B. vSphere Authentication Proxy
C. VMware content library
D. vCenter Server Appliance''':'A',
            '''What are two components of a VM-Host affinity rule? (Choose two.)
A. Host Group
B. Cluster settings
C. VM restart priority
D. VM restart action
E. VM Group''':'AE',
            '''What does ESXi Autoconfiguration do?
A. sets up host profiles
B. configures system network and storage devices
C. determines the number of hosts to be deployed
D. configures Auto Deploy''':'B',
            '''An administrator is using vSphere Web Client to configure the firewall to allow specific third-party
application SSH access to an ESXi Host.
What is the most secure way to configure the firewall rule?
A. Specify remote IP subnet range in IP List.
B. Use Allow connection from any IP address.
C. Enable lockdown mode.
D. Disable the firewall.''':'A',
            '''In a single cluster VM encryption scenario, which two VMs should be excluded from encryption?
(Choose two.)
A. Platform Services Controller
B. vSphere Replication Appliance
C. vRealize Operations Manager
D. VMware vCenter Server
E. vRealize Log Insight''':'BD',
            '''Which vSphere feature is designed to distribute space usage and I/O load across multiple datastores?
A. Storage Policies
B. vStorage API for Array Integration
C. Storage I/O Control
D. vSphere Storage DRS''':'D',
            '''A vSphere administrator creates a VM with 2 vCPUs and 4GB memory. A 3GB memory reservation is
applied to the VM.
What size is .vswp file when the VM is powered on?
A. 1GB
B. 2GB
C. 3GB
D. 4GB''':'A',
            '''An administrator suspects poor VM performance. The administrator runs esxtop and sees the
following output from the CPU and memory screens:
What can the administrator conclude from this output?
A. The host has too many worlds running.
B. The host is ballooning.
C. The host has adequate memory.
D. The host is under CPU pressure.''':'C',
            '''Which teaming and failover policy offers the lowest latency when a failover or a migration with vSphere
vMotion occurs?
A. Network failure detection
B. Fallback
C. Notify switches
D. Load balancing''':'C',
            '''Which two features should an administrator use to protect a VMware vCenter Server Appliance from
host and hardware failures? (Choose two.)
A. VMware Distributed Power Management
B. vCenter High Availability
C. vSphere High Availability
D. vSphere Fault Tolerance
E. VMware vSphere Distributed Resource Scheduler''':'BD',
            '''Which DCUI option determines the time frame an administrator has to log in to the ESXI Shell after
enabling the service?
A. Idle Timeout
B. Availability Timeout
C. Enable SSH
D. Enable ESXi Shell''':'B',
            '''Which two VMware solutions track and analyze the operation of multiple data sources? (Choose two.)
A. vRealize Log Insight
B. vRealize Operations Manager
C. vRealize Life Cycle Manager
D. vRealize Automation
E. vRealize Orchestrator''':'AB',
            '''A vSphere administrator is performing a greenfield vSphere deployment with these requirements:
Which vCenter Server Appliance deployment size meets requirements?
A. Large
B. Tiny
C. Medium
D. Small''':'D',
            '''What is used by a VM for direct access to a LUN?
A. vSAN
B. RDM
C. NVMe
D. ext3''':'B',
            '''A vSphere administrator uses a Dedicated Failover Hosts Admission Control Policy in a cluster. An
ESXi host fails and vSphere HA attempts to restart the VMs onto the dedicated failover hosts. The hosts
have insufficient resources.
'What happens to the VMs?
A. vSphere HA restarts VMs in another cluster.
B. vSphere HA suspends the VMs until a host is available.
C. vSphere HA powers down the VMs.
D. vSphere HA attempts to restart the VMs on other hosts in the cluster.''':'D',
            '''Which migration technique could be used to move a VM between vCenters while the VM is powered
on?
A. Suspended
B. Shared-nothing vSphere vMotion
C. Cold
D. Storage vMotion''':'D',
            '''A VSS is configured with two uplinks and assigned a load balancing policy route based on a virtual port
ID.
What are two potential disadvantages of this configuration? (Choose two.)
A. A VM with a single MAC address is limited to the speed of the uplink associated with the relevant port
ID.
B. Higher resource consumption compared to other load balancing algorithms will occur.
C. The virtual switch is unaware of uplink load and uplinks might become overloaded.
D. The NIC with less load is more likely to be chosen if port IDs match.
E. ESXi will use NIOC to attempt to mitigate network congestion when an uplink becomes saturated.''':'AC',
            '''Which permission should be granted to a user with Administrator permission and with no access to the
encrypted VM console?
A. New role with no Cryptographic Operations
B. Administrator role and Read Only Role
C. Administrator role
D. No Cryptography Administrator role''':'D',
            '''Which feature allows a vSphere administrator to reduce power consumption on a cluster?
A. WOL
B. BMC
C. DPM
D. DNS''':'C',
            '''An administrator manages a cluster containing Production and Test VMs. Production VMs run on a
VSS port group and a storage array separate from the Test VMs. The administrator wants to prevent large
(>500GB) file transfers in Test from impacting Production.
Which two configuration changes should the administrator make to achieve this? (Choose two.)
A. Migrate the VSS port groups to VDS port groups.
B. Install a second virtual NIC in the Production VMs.
C. Move the Production VMs to a resource pool with a memory reservation.
D. Enable the Test VMs to a dedicated folder with CPU shares set to low.''':'AB',
            '''The VM storage policy compliance status is out of date.
Which step should the administrator take to maintain compliance with the existing storage policy?
A. Change the service level capability.
B. Assign a new storage policy.
C. Reapply the storage policy.
D. Migrate VM to another host.''':'C',
            '''A vSphere administrator has a VM that needs to be deployed from a template located in an optimized
content library.
What needs to be done before the VM can be deployed?
A. Export the template as an OVF.
B. Clone the template to a new template.
C. A subscribed content library needs to be created.
D. Deploy VM from the template.''':'C',
            '''A vSphere administrator has the privilege Content library > Add library item on the vCenter object, but
is unable to add items to a local content library.
How would the vSphere administrator correct this?
A. Remove the No Access role on the vCenter object.
B. Restart the Content Library Service.
C. Assign the privilege to the global root object.
D. Reboot the vCenter Server Appliance.''':'C',
            '''What should the administrator do to monitor the size of the VM snapshot?
A. Use native Guest OS monitoring tools.
B. Install VMware Tools.
C. Create a condition-based alarm.
D. Run esxtop.''':'C',
            '''An administrator is elevating the security posture of a vSphere environment after a recent data breach.
All VMs will be encrypted as part of this plan.
Which additional component is required for the encryption?
A. KMS server
B. two-factor authentication
C. encrypted vSphere vMotion
D. vSAN encryption''':'C',
            '''How is vCenter HA different from vSphere HA?
A. vCenter HA requires only an active and passive node.
B. vCenter HA requires an external Platform Services Controller.
C. vCenter HA requires Fault Tolerance.
D. vCenter HA requires an active, passive, and witness node.''':'D',
            '''Which file extension can export host customization for host profiles?
A. .xls
B. .xml
C. .csv
D. .json''':'C',
            '''A vSphere administrator notices performance issues with the vCenter Server Appliance. The CPU
usage is over 70%.
Which two actions should the administrator take to investigate the performance issues? (Choose two.)
A. Verify if all hosts are in a connected state.
B. Use esxtop to identify which process are using high CPU.
C. Use vimtop to identify which processes are using high CPU.
D. Check the vCenter HA configuration.
E. Check if vCenter Server is swapping.''':'CE',
            '''A vSphere Administrator is receiving complaints a database VM is experiencing performance issues.
The VM is a member of the high priority resource pool and the cluster has not experienced contention.
Which condition should be checked to address immediate performance concerns?
A. VM snapshots
B. VMFS version
C. Resource Pool share value
D. Configured CPU shares''':'C',
            '''What could cause a high %RDY value?
A. Incompatible network driver
B. memory fully allocated
C. too many vCPUs configured
D. disk latency greater than 2ms''':'C',
            '''A vSphere Administrator wants to move a vCenter Server with an external Platform Services Controller
from one SSO domain to another SSO domain.
Which option in cmsso-util will achieve this?
A. domain-repoint
B. reconfigure
C. unregister
D. repoint''':'A',
            '''Using vSphere HA Orchestrated Restart an administrator places the most mission critical VM in the
highest priority. After a host failure, the highest priority VM fails to restart while VMs in high priority restart.
What would cause this to occur?
A. There are insufficient cluster resources.
B. Performance degradation VMs tolerate threshold is at default.
C. VMware Tools is not installed.
D. Proactive HA is disabled.''':'D',
            '''An administrator wants to ensure the VMs for two different departments are separated on a single
broadcast domain.
Which configuration fulfills this requirement?
A. PVLAN on Uplink Port
B. PVLAN on VMkernel Interface
C. PVLAN on VSS
D. PVLAN on VDS''':'D',
            '''A vSphere administrator wants to enable Proactive HA in a vSphere cluster.
What is required to use this feature?
A. vROps must be installed.
B. DRS must be enabled.
C. DCUI must be enabled.
D. VCHA must be configured.''':'B',
            '''A vSphere administrator is trying to create a resource pool but the option is grayed out.
What must be enabled before creating a resource pool?
A. DRS
B. Storage DRS
C. EVC
D. HA''':'A',
            '''An administrator is concerned about the amount of time the IT team takes to create multiple VLANs in
a very dynamic vSphere environment.
The environment has these parameters:
How can the administrator centralize the virtual networking configuration so the IT team utilizes time more
efficiently?
A. Deploy a vRealize Orchestrator (vRO) appliance.
B. Create and use a vSphere Distributed Switch (VDS).
C. Enable and configure Storage I/O Control (SIOC).
D. Enable and configure vSphere Network I/O Control (NIOC).''':'B',
            '''A cluster contains database VMs which have low utilization, except during a weekly data load that
causes extremely high utilization.
As DRS balances the VM load, there is an extended period of slow performance.
Which two actions could be taken to reduce the impact of the recurring data load? (Choose two.)
A. Increase the number of vCPUs on the database VMs.
B. Enable VMware vRealize Operations Manager Integration with VMware vCenter.
C. Enable Proactive HA on the cluster.
D. Enable Predictive DRS on the cluster.
E. Increase the RAM allocated to the database VMs.''':'BD',
            '''A vSphere Administrator configures Quick Boot to restart an ESXi host without rebooting the physical
hardware.
In order to troubleshoot any ESXi Quick Boot issues which log file needs to be reviewed?]
A. vmkeventd.log
B. vmkernel.log
C. vpxa.log
D. loadESX.log''':'D',
            '''An administrator decides to implement vSphere networking using the VDS.
Which binding option should the administrator use to manage the VMs if vCenter becomes unavailable?
A. static
B. port
C. ephemeral
D. dynamic''':'C',
            '''A vSphere administrator configures log forwarding for remote syslog server in a vCenter Server
Appliance (VCSA) through the vCenter Server Appliance Management Interface (VAMI).
What is the maximum number of remote syslog servers that can be configured?
A. 1
B. 2
C. 3
D. 4''':'C',
            '''A vSphere administrator needs to migrate VMs in the same vCenter from New York to California due to
impending severe weather.
Which migration should the administrator perform without causing VM downtime?
A. Long Distance vMotion
B. Storage vMotion
C. Cold migration
D. Cross vCenter vMotion''':'A',
            '''Which vSphere APIs support storage hardware acceleration?
A. vSphere APIs for Storage Awareness (VASA)
B. vSphere APIs for I/O Filtering (VAIO)
C. VMware vStorage APIs for Data Protection (VADP)
D. VMware vSphere Storage APIs Array Integration (VAAI)''':'D',
            '''A vSphere administrator discovers the size of the .vswp file for a VM with 2 vCPUs and 4GB of
memory is zero.
What could be the cause?
A. All VM memory is reserved.
B. Memory reservation is not set.
C. VM is running on a snapshot.
D. VM is in a suspended state.''':'A',
            '''Which action should be taken to secure ISCSI devices in a vSphere environment?
A. Require Secure Remote Protocol.
B. Require ESXi hosts to use ISCSI port binding.
C. Require vCenter Enhanced Linked Mode.
D. Require ESXi hosts to authentication to the target.''':'D',
            '''What are two advantages of deploying a VDS as compared to a VSS? (Choose two.)
A. Data center setup and administration are simplified by centralizing network configuration.
B. There is IPv6 support for a VDS.
C. 802.1Q tagging support is available.
D. Uplinks are allowed to be configured in an Active/Standby configuration.
E. Ports migrate with their clients.''':'AE',
            '''A vSphere administrator has renamed the inventory name of a virtual machine.
Which task should the administrator perform to ensure the virtual machine files are also renamed to
match the new virtual machine name?
A. Take a virtual machine snapshot.
B. Unregister and register the virtual machine in vCenter Server.
C. Migrate the machine to another host with vSphere vMotion.
D. Migrate the machine to another datastore with Storage vMotion''':'D',
            '''An administrator needs to identify where the VM encryption settings are stored.
Which file stores the encryption setting?
A. .vmdk
B. .vmsd
C. .nvram
D. .vmx''':'D',
            '''In a vSphere HA enabled cluster, what happens if the master host is unable to communicate with a
slave host over the management network?
A. The host is dropped from the cluster.
B. The master host uses datastore heartbeating.
C. A new master host is elected.
D. VM are rebooted by vSphere HA.''':'D',
            '''Where is vCenter SSO configured?
A. In the service console
B. In the DCUI
C. In the vSphere client
D. In the host client''':'C',
            '''Which VM storage policy rule category ensures all VMs for a department are on the same datastore?
A. Capability
B. Data Service
C. Host
D. Tag''':'D',
            '''After installing vCenter, which two identity sources and users are available by default? (Choose two.)
A. vsphere.vclass
B. Active Directory
C. vsphere.local
D. vIDM
E. localos''':'CE',
            '''A vSphere administrator has configured software iSCSI port binding in the environment with two
VMkernel ports and four target portals.
How many iSCSI sessions would be created from bound ports to targets?
A. 2
B. 4
C. 8
D. 16''':'C',
            '''A vSphere administrator is required to join all strategies ESXi hosts to an Active Directory domain for
enhanced security.
Which utility would accomplish this?
A. Unified Access Gateway
B. vSphere Update Manager
C. vSphere Authentication Proxy
D. vSphere Auto Deploy''':'C',
            '''An administrator runs multiple clusters spread across multiple vCenters. The administrator needs to be
able to migrate any VM to any cluster.
On which two vCenter Server objects could the administrator configure EVC mode to fulfill this
requirement? (Choose two.)
A. VM
B. resource pool
C. datacenter
D. cluster
E. folder
Answer: A,D''':'AD',
            '''Which rule should be used in an SDRS environment to create a VM requiring virtual disks be kept on
different datastores?
A. VM Anti-Affinity Rule
B. Intra-VM VMDK Affinity Rule
C. VM-Host Affinity Rule
D. Intra-VM VMDK Anti-Affinity Rule''':'D',
            '''What should be installed on a VM to enhance performance and enable additional features?
A. RAMmap
B. PsInfo
C. Process Monitor
D. VMware Tools''':'D',
            '''Which two availability features require a VM restart for recovery? (Choose two.)
A. vSphere DPM
B. vSphere vMotion
C. vSphere Replication
D. vSphere Fault Tolerance
E. vSphere HA''':'CE',
            '''A vSphere Administrator wants to convert a vCenter Server instance with an external Platform
Services Controller to an embedded Platform Services Controller instance.
Which tool should be used to accomplish this?
A. VMware vCenter Converter
B. CloudClient Utility
C. Convergence Utility
D. Cmsso-util Utility''':'C',
            '''An administrator runs vSphere Infrastructure in the following configuration:
The administrator wants to use host profiles to manage the hosts.
Where should the administrator attach the host profile?
A. vCenter object
B. each cluster
C. each data center
D. each folder''':'B',
            '''A customer is experiencing a network performance problem and is using the esxtop utility to determine
the cause. Esxtop reveals no dropped packets.
Which two conditions should the customer check? (Choose two.)
A. packet size
B. data receive rate
C. IPv6 support
D. CPU contention''':'BD',
            '''A new AD domain has just been added to vSphere as an identity source. This new domain has a user
group called administrators group.
Which role do the administrators group users have by default, when authenticated to vCenter Server?
A. Read Only
B. No Cryptography Administrator
C. Administrator
D. No Access''':'C',
            '''A vSphere administrator has to forward vCenter Server logs to a syslog server to be retained for
security audits.
Which two protocols are available in vCenter Server Appliance VAMI for syslog forwarding? (Choose
two.)
A. HTTPS
B. SSL
C. DTLS
D. UDP
E. TLS''':'DE',
            '''A cluster of vSphere 6.5 and 6.7 hosts all have identical hardware. VMs are created on the 6.7 hosts
with virtual hardware version 14. During routine maintenance on the 6.7 hosts, the VMs are unable to
migrate to the 6.5 hosts.
Why are the VMs unable to migrate to the 6.5 hosts?
A. The virtual hardware version is incompatible with 6.5
B. VMware Tools version is upgraded
C. EVC mode is disabled
D. DPM is configured incorrectly''':'C',
            '''Which optional module of vSphere Update Manager supports patch recalls and notifications?
A. VMware vSphere Update Manager Download Service
B. vCenter Server Lifecycle Manager Service
C. vSphere Auto Deploy
D. VMware vSphere Update Manager Extension''':'A',
            '''What is the outcome when two affinity rules conflict?
A. VMs will continue to migrate
B. Rules are applied based on priority
C. Only one rule can be enabled
D. Random rule enablement occurs''':'C',
            '''A vSphere administrator needs to quickly move a critical VM from an AMD-cluster to an Intel-cluster.
How can the vSphere administrator move the VM?
A. vSphere Storage vMotion
B. vSphere encrypted vMotion
C. vSphere vMotion
D. Cold Migration''':'D',
            '''A VM is created with a thin provisioned disk.
Which two requirements are needed to inflate the disk? (Choose two.)
A. Right click .vmx and select Inflate
B. Right click .vmdk and select Inflate
C. Reboot the VM
D. Power off the VM
E. Edit the .vmdk file''':'BD',
            '''What would cause an administrator to encounter a remote device backing error while running
vMotion?
A. VM running on too many snapshots
B. Host CD-ROM attached to VM
C. Virtual mode RDM attached to VM
D. Host USB device attached to VM''':'B',
            '''Which host profile operation can be scheduled?
A. Check Host Profile Compliance
B. Apply Host Profile
C. Remediate a Profile
D. Detach Host Profile''':'A',
            '''An ESXi host with default settings is currently in normal lockdown mode.
Which action is granted to users with Administrator privileges on the host without adding them to the
Exception User list?
A. Access the host using the vCenter Server
B. Access the host using an SSH session
C. Access the host using the Host Client
D. Access the host using the ESXi Shel''':'A',
            '''What could a vSphere administrator use to move a group of VMs to another port group?
A. Network I/O Control
B. IP hash
C. Network Port Binding
D. vSphere vMotion''':'D',
            '''Per a customer request, a vSphere administrator increases the number of vCPUs in several VMs
within a cluster. After the vCPU increase, the upgraded VMs exhibit slower performance. The vSphere
administrator uses esxtop to check ESXi host performance.
Which two counters should be checked to detect CPU overcommitment? (Choose two.)
A. %SWPWT
B. %USED
C. %MLMTD
D. %SYS
E. %RDY''':'BE',
            '''A vSphere administrator has a requirement to move virtual machines between vCenter Servers using
vSphere Client.
Which condition should be met for the Cross vCenter Server vMotion to succeed?
A. vCenter Servers must be time-synchronized
B. vCenter Servers should be appliances
C. vCenter Servers should be in different vCenter Single Sign-on domains
D. vCenter Servers should be on the same version''':'A',
            '''Which command should be used to monitor free disk space on a vCenter Server Appliance?
A. df
B. esxtop
C. cloudvm-ram-size
D. vimtop''':'A',
            '''An application requires a high network transmission rate and multiple simultaneous TCP streams.
What is the maximum number of threads that can be created per vNIC?
A. 4
B. 6
C. 8
D. 10''':'D',
            '''A vSphere administrator has disabled Fault Tolerance on a powered-off VM.
What could cause the VM to fail to power back on?
A. insufficient CPU resources
B. VM shares
C. VM limits
D. insufficient memory resources''':'D',
            '''An ESXi host is limited to two 1GbE physical NICs to support VM traffic.
Which VDS teaming policy should be chosen to ensure maximum availability across both uplinks?
A. Route Based on IP Hash
B. Route Based on Originating Virtual Port
C. Route Based on Physical NIC Load
D. Route Based on Source MAC''':'C',
            '''An administrator manages a team that regularly deploys many similar Windows VMs in the
environment.
Which action should be taken to improve efficiency of this process?
A. take VM snapshots
B. use the New Virtual Machine wizard
C. deploy from a VM template
D. restore from a VM backup''':'C',
            '''An administrator enables DRS and sets the automation level to Fully Automated. DRS is only making
initial placement recommendations.
What is causing this?
A. DRS is set to aggressive
B. HA is disabled on the cluster
C. The VMs have virtual flash reservations
D. vMotion network is misconfigured''':'A',
            '''When enabled, what ensures only signed drivers can load into a virtual machine?
A. Secure Boot
B. lockdown mode
C. micro-segmentation
D. TPM''':'A',
            '''An administrator configures vSphere Replication for a DR site.
Which two items should be deployed at the second site? (Choose two.)
A. array-based storage
B. vSphere Replication appliance
C. vCenter Server
D. vSphere Distributed Switch (VDS)
E. vSphere Data Protection (VDP)''':'BC',
            '''Which Network Failure Detection Policy will prevent network failover?
A. Notify Switches Policy
B. Link status only
C. Failback Policy
D. Beacon probing''':'B',
            '''A customer suspects someone or something is changing the MAC address of a virtual machine.
Which security policy should the customer modify to obtain more information?
A. MAC Address Change
B. Promiscuous Mode
C. Discovery Protocol
D. Forged Transmits''':'A',
            '''A vSphere administrator attempts to create a VM-VM affinity rule but is unable to locate the option in
the vSpehre Client.
What would cause this to happen?
A. vSphere DRS is disabled
B. vSphere DRS is set to manual
C. Admission control is not enabled
D. Affinity rules are only managed using the Host Client''':'A',
            '''Which policy is used for intelligent optimization of network interface traffic on a vSphere Distributed
Switch (VDS)?
A. Route Based on IP Hash
B. Route Based on Source MAC Hash
C. Route Based on Physical NIC Load
D. Route Based on Originating Virtual Port''':'C',
            '''A vSphere administrator wants to ensure provisioned virtual machine storage objects are allocated to
guarantee a service level agreement.
Which feature would accomplish this?
A. Storage policy
B. VAIO Filtering
C. Storage I/O Control
D. Storage DRS''':'D',
            '''A host profile is created from a reference host in Cluster A and applied to all hosts in the same cluster.
What effect is expected when the administrator updates the DNS settings on the reference host?
A. DNS settings are updated for all hosts in the cluster
B. The reference host becomes non-compliant
C. The reference host enters maintenance mode
D. The host profile is updated automatically''':'B',
            '''An administrator is unable to use the vSphere Client shutdown option on a Windows VM.
What should be installed to correct this?
A. Autologon
B. Windows Updates
C. PortMon
D. VMware Tools''':'D',
            '''An administrator manages a vSphere environment with the following configuration:
The administrator notices that occasionally the VM with the memory reservation fails to restart during an
HA host failure event.
What could cause this to happen?
A. Failover capacity is exceeded due to the memory reservation
B. vMotion network needs more bandwidth to restart the reserved VM
C. VMs with reservations must be in their own dedicated cluster
D. DRS must be enabled when admission control is enabled''':'A',
            '''A vSphere Administrator wants to group virtual machines by guest operating system type in vCenter
Server.
Which feature would accomplish this?
A. Custom Attributes
B. vSphere Tags
C. Enhanced Linked Mode
D. vFRC''':'B',
            '''An application owner complains about poor performance on a VM named APPVM01.
Troubleshooting indicates that another VM named DBVM01 on the same datastore is saturating the
volume with I/O requests.
Which two actions can be taken to reduce DBVM01 impact on APPVM01, while still prioritizing DBVM01
disk I/O? (Choose two.)
A. Configure APPVM01 with a shares limit of Low, and DBVM01 with a shares limit of Normal
B. Enable Network I/O Control on the cluster containing APPM01 and DBVM01
C. Enable Storage I/O Control on the cluster containing APPVM01 and DBVM01
D. Enable Storage I/O Control on the datastore containing APPM01 and DBVM01
E. Configure APPVM01 with a shares limit of High, and DBVM01 with a shares limit of Normal''':'DE',
            '''Which two options are available for a vSphere administrator to install ESXi on a host? (Choose two.)
A. vSphere Replication
B. VMware Workspace ONE
C. vSphere Update Manager
D. Interactive Mode
E. vSphere Auto Deploy''':'CE',
            '''What are two features of the CPU scheduler? (Choose two.)
A. allocates CPU and memory resource usage
B. determines which worlds are entitled to CPU time
C. schedules vCPUs on physical CPUs
D. creates a world for each virtual machine to run it
E. checks CPU uptime''':'AC',
            '''Which condition would prevent a vSphere Administrator from increasing the vCPU on a virtual
machine to 128 vCPUs?
A. CPU Affinity is enabled on the virtual machine
B. The host is running on the Enterprise license
C. There are too few logical cores on the host
D. Hyper-threading is enabled on the host''':'C',
            '''Which vSphere Update Manager baseline type is used for scanning and remediating objects
third-party device drivers?
A. upgrade
B. extension
C. patch
D. predefined''':'B',
            '''How should an administrator assign a user the Administrator permission without encryption-related
rights?
A. Grant the user the Virtual Machine Power User role
B. Grant the user the No Cryptography Administrator role
C. Grant the user the Administrator role
D. Grant the user No Access role on encrypted VMs''':'B',
            '''A vSphere administrator is installing ESXi 6.7 on a diskless host booting from an onboard 8GB SD
card.
What should be done to ensure log files are persisted through a host reboot?
A. Manually create scratch partition on the SD card
B. By default the log files will be stored on the SD card
C. Ensure vCenter Dump Collector service is running
D. Configure the scratch partition to use an available datastore''':'D',
            '''A VM is experiencing inconsistent network connectivity between two ESXi hosts connecting to the
same physical switches. The effect of the inconsistency is this:
The vSphere administrator wants to ensure the physical switches connecting to the ESXi are configured
correctly.
How can this be accomplished?
A. Use Network Health Check to verify the VLAN trunks on VSS
B. Use vSphere Health Check to verify on MTU settings on VDS
C. Use Network Health Check to verify the VLAN trunks on VDS
D. Use Network Health Check to verify MTU settings on VSS''':'D',
            '''What provides certificate and license management services?
A. Auto Deploy
B. Unified Access Gateway
C. vCenter Service
D. Platform Services Controller''':'D',
            '''Which two actions should an administrator take to ensure a VM has the highest networking
bandwidth? (Choose two.)
A. Configure traffic shaping
B. Configure LACP
C. Configure resource pools
D. Configure shares, reservations, and limits
E. Configure marking and filtering''':'BC',
            '''Which two infrastructure services are provided by the Platform Services Controller? (Choose two.)
A. Auto Deploy
B. License Service
C. vCenter Single Sign-On
D. vSphere Syslog Collector
E. vSphere Web Client''':'BC',
            '''Which setting should be used to exclude one hard disk from VM snapshots?
A. Thin Provision disk type
B. Dependent disk mode
C. Independent disk mode
D. Passthrough device mode''':'C',
            '''Which native feature could be used to protect virtual machine files and disks containing confidential
customer data?
A. VMware Tools
B. vCenter HA
C. VM encryption
D. VDP''':'C',
            '''What is the default vCenter Server for a new user?
A. No Access
B. No Cryptography Administrator
C. Read-Only
D. Administrator''':'A',
            '''Which condition would be prevent a vSphere Administrator from increasing the vCPU on a virtual
machine to 128 vCPUs?
A. CPU Affinity is enabled on the virtual machine.
B. The host is running on the Enterprise license.
C. Hyper-threading is enabled on the host.
D. There are too few logical cores on the host.''':'D',
            '''What is required to convert a VM to a template?
A. Power off the virtual machine.
B. Choose a thin-provisioned format.
C. Reregister the template.
D. Select a storage policy.''':'A',
            '''A vCenter High Availability cluster consists of how many vCenter Server Appliance instances?
A. 2
B. 3
C. 4
D. 5''':'B',
            '''What happens within the network when a customer uses a vSphere Distributed Switch (VDS) and
vCenter is offline?
A. An isolation event occurs.
B. Network is lost.
C. Packets continue to be forwarded.
D. Network runs with intermittent failures.''':'C',
            '''An administrator is planning maintenance for a cluster with the following configuration:
- DRS is fully automated
- Dedicated 10GbE vMotion network
- iSCSI storage with CHAP
When a host is placed into maintenance mode, what is the maximum number of supported concurrent
vMotion operations?
A. 4
B. 6
C. 8
D. 10''':'C',
            '''VMs are violating affinity rules and DRS is unable to correct the rules violations.
Which two actions should an administrator take to identify why DRS is unable to satisfy the affinity rules?
(Choose two.)
A. Review VM Overrides tab.
B. Review systems logs.
C. Review if violated rules are in vCenter VAMI.
D. Review Faults tab in DRS.
E. Review VM OS logs.''':'AD',
            '''A user asks for a VM to be deployed that must remain on the same host at all times.
How should DRS be configured for the VM?
A. Use cluster settings
B. Partially Automated
C. Fully Automated
D. Disabled''':'D',
            '''A user logs in to vCenter Server as an administrator and is unable to view Single Sign On
Configuration.
Which vCenter Single Sign On group should the administrator belong to, to view Single Sign On
Configuration?
A. ComponentManager.Administrators
B. Administrators
C. SystemConfiguration.Administrators
D. SystemConfiguration.BashShellAdministrators''':'C'}
questions = list(topic.keys())
def show_menu():
    cmds = {'0': Exercise_mode, '1': Examination_mode}
    prompt = '''    Welcome  !!!
(0) 练习模式
(1) 考试模式(随机选题，按Q，q统计分数或最后统计分数)
(2) 退出
请选择(0/1/2): '''
    while True:
        subprocess.call("clear")
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效选择，请重试！')
            continue
        if choice == '2':
            print('Bye-bye')
            break
        cmds[choice]()


def Exercise_mode():
    while True:
        # os.system('cls')
        subprocess.call("clear")
        question = random.choice(questions)
        print(question)
        print(' ')
        answer = input('Your answer >> '  ).strip()
        if answer == topic[question] or answer ==topic[question].lower():
            print('\033[32;1mYou are right !!!\033[0m')
        else:
            print('\033[31;1mError,Answer is %s !!!\033[0m' %  topic[question])
        go = input('(Enter or arbitrarily to next), (Q to quit)>> ').strip()
        if go == 'Q':
            break

def Examination_mode():
    result = 0
    b = 0
    chs = random.sample(questions,120)
    for i in chs:
        # subprocess.call("clear")
        print(i)
        print(' ')
        answer = input('Your answer >>  ').strip()
        if answer == topic[i] or answer == topic[i].lower():
           result += 1
           print('\033[32;1mYou are right !!!\033[0m')
           print(' ')
           print(' ')
        elif answer in ['q','Q']:
           break
        else:
            b += 1
            # with open('error.log', 'wb') as fobj:
            #     while True:
            #         data = i.read(4096)
            #         if not data:
            #             break
            #         fobj.write(data)
            print('\033[31;1mError,answer is %s !!!\033[0m' % topic[i])
            print(' ')
            print(' ')
    a = b + result
    print('\033[32;1mThere are %s problems,You got %s right!\033[0m' % (a,result) )
    # bye = input('(Enter or arbitrarily to contine), (Q to quit)>> ').strip()
    # if bye == 'Q':
    #     return
    go = input(' ')
if __name__ == '__main__':
    try:
      show_menu()
    except (KeyboardInterrupt, EOFError):
      print('\nBye-bye')
