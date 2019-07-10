#!/usr/bin/env python
import inspect

from vmcjp.network.security_groups import get_security_group_ids_and_names
from vmcjp.utils.metadata import get_members
from vmcjp.utils.listutils import compare_list_and_dict
from vmcjp.utils.stringutils import replace_strings_in_list

def get_firewall_rules(gateway_type, nsx_client):
  admin_user = set(["admin", "admin;admin"])
  
  security_groups = get_security_group_ids_and_names(gateway_type, nsx_client)
#  print(security_groups)

  policies = nsx_client.infra.domains.GatewayPolicies.get(gateway_type, "default")
#  print(policies.to_dict())

  gw_dn = policies.get_field("display_name")
  rules = policies.get_field("rules")

  rules_list = [
    get_rules(rule, gateway_type, security_groups) 
    for rule in rules
    if rule.get_field("create_user") not in admin_user
  ]
#  print(rules_list)
#  get_members(rule)

  return {"display_name": gw_dn, "rules": rules_list}

def get_rules(rule, gateway_type, security_groups):
  sn = rule.get_field("sequence_number")
  source_groups = rule.get_field("source_groups")
  sg = replace_strings_in_list(source_groups, "/infra/domains/" + gateway_type + "/groups/")
  sg_names = compare_list_and_dict(sg, security_groups)
  dest_groups = rule.get_field("destination_groups")
  dg = replace_strings_in_list(dest_groups, "/infra/domains/" + gateway_type + "/groups/")
  dg_names = compare_list_and_dict(dg, security_groups)

  return {"create_user": rule.get_field("create_user"),
          "display_name": rule.get_field("display_name"),
          "logged": rule.get_field("logged"),
          "destination_groups": dest_groups,
          "destination_groups_names": dg_names,
          "scope": rule.get_field("scope"),
          "services": rule.get_field("services"),
          "sequence_number": sn,
          "action": rule.get_field("action"),
          "source_groups": source_groups,
          "source_group_names": sg_names}
