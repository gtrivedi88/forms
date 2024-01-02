 gtrivedi@gtrivedi-thinkpadt14sgen1  ~/.crc/cache  oc patch consoles.operator.openshift.io cluster --patch '{ "spec": {"managementState": "Unmanaged" } }' --type=merge
console.operator.openshift.io/cluster patched (no change)
 gtrivedi@gtrivedi-thinkpadt14sgen1  ~/.crc/cache  oc set image deploy console console=quay.io/openshift/origin-console:latest -n openshift-console
