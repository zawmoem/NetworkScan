from netmiko import SSHDetect

device_list = {"cisco_asa":[],"cisco_ios":[],"cisco_nxos":[],"juniper_junos":[]}

def detectdevice (ip_addr,uname,pwd):
	defineDev = SSHDetect(host=ip_addr,username=uname,password=pwd,device_type="autodetect")
	devType = defineDev.autodetect()
	defineDev.potential_matches
	device_list[devType].append(ip_addr)

if __name__ == "__main__":

	#"""
	active_hosts = {"active_ip_addrs": [
	"192.168.0.2",
	"192.168.0.1",
	"192.168.0.10"
	]}
	#"""
	
	# Create multiple thread for concurrent ssh sessions	
	executor = concurrent.futures.ThreadPoolExecutor(254)
	identifyType = [executor.submit(detectdevice, str(ip),inputUserName,inputPassword) for ip in active_hosts["active_ip_addrs"]]
	
	#To wait until all thread to be completed
	executor.shutdown(wait=True, cancel_futures=True)

	#Combine all resutls to JSON output
	json_devices = json.dumps(device_list, indent=1)

	print(json_devices)


"""
a10
accedian
adtran_os
adva_fsp150f2
adva_fsp150f3
alcatel_aos
alcatel_sros
allied_telesis_awplus
apresia_aeos
arista_eos
arris_cer
aruba_os
aruba_osswitch
aruba_procurve
audiocode_66
audiocode_72
audiocode_shell
avaya_ers
avaya_vsp
broadcom_icos
brocade_fastiron
brocade_fos
brocade_netiron
brocade_nos
brocade_vdx
brocade_vyos
calix_b6
casa_cmts
cdot_cros
centec_os
checkpoint_gaia
ciena_saos
cisco_asa
cisco_ftd
cisco_ios
cisco_nxos
cisco_s200
cisco_s300
cisco_tp
cisco_viptela
cisco_wlc
cisco_xe
cisco_xr
cloudgenix_ion
coriant
dell_dnos9
dell_force10
dell_isilon
dell_os10
dell_os6
dell_os9
dell_powerconnect
dell_sonic
dlink_ds
digi_transport
eltex
eltex_esr
endace
enterasys
ericsson_ipos
ericsson_mltn63
ericsson_mltn66
extreme
extreme_ers
extreme_exos
extreme_netiron
extreme_nos
extreme_slx
extreme_tierra
extreme_vdx
extreme_vsp
extreme_wing
f5_linux
f5_ltm
f5_tmsh
flexvnf
fortinet
generic
generic_termserver
hillstone_stoneos
hp_comware
hp_procurve
huawei
huawei_olt
huawei_smartax
huawei_vrp
huawei_vrpv8
ipinfusion_ocnos
juniper
juniper_junos
juniper_screenos
keymile
keymile_nos
linux
mellanox
mellanox_mlnxos
mikrotik_routeros
mikrotik_switchos
mrv_lx
mrv_optiswitch
netapp_cdot
netgear_prosafe
netscaler
nokia_srl
nokia_sros
oneaccess_oneos
ovs_linux
paloalto_panos
pluribus
quanta_mesh
rad_etx
raisecom_roap
ruckus_fastiron
ruijie_os
sixwind_os
sophos_sfos
supermicro_smis
teldat_cit
tplink_jetstream
ubiquiti_edge
ubiquiti_edgerouter
ubiquiti_edgeswitch
ubiquiti_unifiswitch
vyatta_vyos
vyos
watchguard_fireware
yamaha
zte_zxros
zyxel_os
"""
