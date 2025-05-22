# Cisco DNA Center API Endpoints

## Table of Contents

- [Appliance](#appliance)
  - [Cisco IMC](#cisco-imc)
- [Authentication](#authentication)
  - [](#)
- [Cisco DNA Center System](#cisco-dna-center-system)
  - [Disaster Recovery](#disaster-recovery)
  - [Health and Performance](#health-and-performance)
  - [Licenses](#licenses)
  - [Platform](#platform)
- [Connectivity](#connectivity)
  - [Fabric Wireless](#fabric-wireless)
  - [SDA](#sda)
  - [Wired](#wired)
  - [Wireless](#wireless)
- [Ecosystem Integrations](#ecosystem-integrations)
  - [ITSM](#itsm)
- [Event Management](#event-management)
  - [](#)
- [Integrations](#integrations)
  - [ITSM Integration](#itsm-integration)
- [Know Your Network](#know-your-network)
  - [](#)
  - [Applications](#applications)
  - [Clients](#clients)
  - [Compliance](#compliance)
  - [Devices](#devices)
  - [EoX](#eox)
  - [Issues](#issues)
  - [Security Advisories](#security-advisories)
  - [Sensors](#sensors)
  - [Sites](#sites)
  - [Topology](#topology)
  - [Users](#users)
- [Operational Tasks](#operational-tasks)
  - [Command Runner](#command-runner)
  - [Discovery](#discovery)
  - [File](#file)
  - [Path Trace](#path-trace)
  - [Reports](#reports)
  - [Tag](#tag)
  - [Task](#task)
- [Policy](#policy)
  - [AI Endpoint Analytics](#ai-endpoint-analytics)
  - [Application Policy](#application-policy)
- [Site Management](#site-management)
  - [Configuration Archive](#configuration-archive)
  - [Configuration Templates](#configuration-templates)
  - [Device Onboarding (PnP)](#device-onboarding-(pnp))
  - [Device Replacement](#device-replacement)
  - [LAN Automation](#lan-automation)
  - [Network Settings](#network-settings)
  - [Site Design](#site-design)
  - [Software Image Management (SWIM)](#software-image-management-(swim))
- [System](#system)
  - [Cisco Trusted Certificates](#cisco-trusted-certificates)
  - [Health and Performance](#health-and-performance)
  - [Licenses](#licenses)
  - [User and Roles](#user-and-roles)
- [System Settings](#system-settings)
  - [](#)

## API Endpoints by Domain

### Appliance

#### Cisco IMC

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| DELETE | `/dna/system/api/v1/ciscoImcs/{id}` | deletesTheCiscoIMCConfigurationForACatalystCenterNode | Deletes the Cisco IMC configuration for a Catalyst Center node | id |
| PUT | `/dna/system/api/v1/ciscoImcs/{id}` | updatesTheCiscoIMCConfigurationForACatalystCenterNode | Updates the Cisco IMC configuration for a Catalyst Center node | id |
| GET | `/dna/system/api/v1/ciscoImcs/{id}` | retrievesTheCiscoIMCConfigurationForACatalystCenterNode | Retrieves the Cisco IMC configuration for a Catalyst Center node | id |
| GET | `/dna/system/api/v1/ciscoImcs` | retrievesCiscoIMCConfigurationsForCatalystCenterNodes | Retrieves Cisco IMC configurations for Catalyst Center nodes |  |
| POST | `/dna/system/api/v1/ciscoImcs` | addsCiscoIMCConfigurationToACatalystCenterNode | Adds Cisco IMC configuration to a Catalyst Center node |  |

### Authentication

#### 

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/certificate` | importCertificate | importCertificate | Query: pkPassword, listOfUsers |
| POST | `/dna/intent/api/v1/certificate-p12` | importCertificateP12 | importCertificateP12 | Query: p12Password, pkPassword, listOfUsers |
| POST | `/dna/system/api/v1/auth/token` | authenticationAPI | Authentication API |  |

### Cisco DNA Center System

#### Disaster Recovery

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/disasterrecovery/system/operationstatus` | disasterRecoveryOperationalStatus | Disaster Recovery Operational Status |  |
| GET | `/dna/intent/api/v1/disasterrecovery/system/status` | disasterRecoveryStatus | Disaster Recovery Status |  |

#### Health and Performance

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/diagnosticValidationWorkflows` | retrievesTheListOfValidationWorkflows | Retrieves the list of validation workflows | Query: startTime, endTime, runStatus, offset, limit |
| POST | `/dna/intent/api/v1/diagnosticValidationWorkflows` | submitsTheWorkflowForExecutingValidations | Submits the workflow for executing validations |  |
| GET | `/dna/intent/api/v1/diagnosticValidationSets` | retrievesAllTheValidationSets | Retrieves all the validation sets | Query: view |
| GET | `/dna/intent/api/v1/diagnosticValidationSets/{id}` | retrievesValidationDetailsForAValidationSet | Retrieves validation details for a validation set | id |
| GET | `/dna/intent/api/v1/diagnostics/system/health/count` | systemHealthCountAPI | System Health Count API | Query: domain, subdomain |
| GET | `/dna/intent/api/v1/diagnosticValidationWorkflows/count` | retrievesTheCountOfValidationWorkflows | Retrieves the count of validation workflows | Query: startTime, endTime, runStatus |
| GET | `/dna/intent/api/v1/diagnostics/system/health` | systemHealthAPI | System Health API | Query: summary, domain, subdomain, limit, offset |
| GET | `/dna/intent/api/v1/diagnostics/system/performance/history` | systemPerformanceHistoricalAPI | System Performance Historical API | Query: kpi, startTime, endTime |
| DELETE | `/dna/intent/api/v1/diagnosticValidationWorkflows/{id}` | deletesAValidationWorkflow | Deletes a validation workflow | id |
| GET | `/dna/intent/api/v1/diagnosticValidationWorkflows/{id}` | retrievesValidationWorkflowDetails | Retrieves validation workflow details | id |
| GET | `/dna/intent/api/v1/diagnostics/system/performance` | systemPerformanceAPI | System Performance API | Query: kpi, function, startTime, endTime |

#### Licenses

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/connectionModeSetting` | retrievesCSSMConnectionMode | Retrieves CSSM Connection Mode |  |
| PUT | `/dna/intent/api/v1/connectionModeSetting` | updateCSSMConnectionMode | Update CSSM Connection Mode |  |
| GET | `/dna/system/api/v1/license/lastOperationStatus` | systemLicensingLastOperationStatus | System Licensing Last Operation Status |  |
| GET | `/dna/intent/api/v1/licenses/usage/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name}` | licenseUsageDetails | License Usage Details | smart_account_id, virtual_account_name | Query: device_type |
| GET | `/dna/intent/api/v1/licenses/device/summary` | deviceLicenseSummary | Device License Summary | Query: page_number, order, sort_by, dna_level, device_type, limit, registration_status, virtual_account_name, smart_account_id, device_uuid |
| GET | `/dna/system/api/v1/license/status` | systemLicensingStatus | System Licensing Status |  |
| POST | `/dna/system/api/v1/license/deregister` | smartLicensingDeregistration | Smart Licensing Deregistration |  |
| GET | `/dna/intent/api/v1/licenses/smartAccount/{smart_account_id}/virtualAccounts` | virtualAccountDetails | Virtual Account Details | smart_account_id |
| GET | `/dna/intent/api/v1/licenses/device/count` | deviceCountDetails | Device Count Details | Query: device_type, registration_status, dna_level, virtual_account_name, smart_account_id |
| PUT | `/dna/intent/api/v1/licenseSetting` | updateLicenseSetting | Update license setting |  |
| GET | `/dna/intent/api/v1/licenseSetting` | retrieveLicenseSetting | Retrieve license setting |  |
| PUT | `/dna/intent/api/v1/licenses/smartAccount/virtualAccount/deregister` | deviceDeregistration | Device Deregistration |  |
| PUT | `/dna/intent/api/v1/licenses/smartAccount/virtualAccount/{virtual_account_name}/register` | deviceRegistration | Device Registration | virtual_account_name |
| POST | `/dna/intent/api/v1/licenses/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name}/device/transfer` | changeVirtualAccount | Change Virtual Account | smart_account_id, virtual_account_name |
| GET | `/dna/intent/api/v1/licenses/smartAccounts` | smartAccountDetails | Smart Account Details |  |
| POST | `/dna/system/api/v1/license/renew` | smartLicensingRenewOperation | Smart Licensing Renew Operation |  |
| POST | `/dna/system/api/v1/license/register` | systemLicensingRegistration | System Licensing Registration |  |
| GET | `/dna/intent/api/v1/licenses/device/{device_uuid}/details` | deviceLicenseDetails | Device License Details | device_uuid |
| GET | `/dna/intent/api/v1/licenses/term/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name}` | licenseTermDetails | License Term Details | smart_account_id, virtual_account_name | Query: device_type |

#### Platform

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/dnac-release` | ciscoDNACenterReleaseSummary | Cisco DNA Center Release Summary |  |
| GET | `/dna/intent/api/v1/nodes-config` | ciscoDNACenterNodesConfigurationSummary | Cisco DNA Center Nodes Configuration Summary |  |
| GET | `/dna/intent/api/v1/dnac-packages` | ciscoDNACenterPackagesSummary | Cisco DNA Center Packages Summary |  |

### Connectivity

#### Fabric Wireless

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| PUT | `/dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids` | add,UpdateOrRemoveSSIDMappingToAVLAN | Add, Update or Remove SSID mapping to a VLAN | fabricId |
| GET | `/dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids` | retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite. | Retrieve the VLANs and SSIDs mapped to the VLAN within a Fabric Site. | fabricId | Query: limit, offset |
| PUT | `/dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting` | switchWirelessSettingAndRollingAPUpgradeManagement | Switch Wireless Setting and Rolling AP Upgrade Management | fabricId |
| GET | `/dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting` | getSDAWirelessDetailsFromSwitches | Get SDA Wireless details from Switches | fabricId |
| GET | `/dna/intent/api/v1/sda/fabrics/vlanToSsids/count` | returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping | Return the count of all the fabric site which has SSID to IP Pool mapping  |  |
| POST | `/dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting/reload` | reloadSwitchForWirelessControllerCleanup | Reload Switch for Wireless Controller Cleanup | fabricId |
| GET | `/dna/intent/api/v1/sda/fabrics/vlanToSsids` | returnsAllTheFabricSitesThatHaveVLANToSSIDMapping. | Returns all the Fabric Sites that have VLAN to SSID mapping. | Query: limit, offset |
| PUT | `/dna/intent/api/v1/sda/fabrics/{fabricId}/wirelessMulticast` | updateSDAWirelessMulticast | Update SDA Wireless Multicast | fabricId |
| GET | `/dna/intent/api/v1/sda/fabrics/{fabricId}/wirelessMulticast` | getSDAWirelessMulticast | Get SDA Wireless Multicast | fabricId |
| GET | `/dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids/count` | returnsTheCountOfVLANsMappedToSSIDsInAFabricSite. | Returns the count of VLANs mapped to SSIDs in a Fabric Site. | fabricId |
| DELETE | `/dna/intent/api/v1/business/sda/wireless-controller` | removeWLCFromFabricDomain | Remove WLC from Fabric Domain | Query: deviceIPAddress |
| POST | `/dna/intent/api/v1/business/sda/wireless-controller` | addWLCToFabricDomain | Add WLC to Fabric Domain |  |
| PUT | `/dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool` | updateSSIDToIPPoolMapping | Update SSID to IP Pool Mapping |  |
| GET | `/dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool` | getSSIDToIPPoolMapping | Get SSID to IP Pool Mapping | Query: vlanName, siteNameHierarchy |
| POST | `/dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool` | addSSIDToIPPoolMapping | Add SSID to IP Pool Mapping |  |

#### SDA

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/sda/multicast/virtualNetworks` | addMulticastVirtualNetworks | Add multicast virtual networks |  |
| GET | `/dna/intent/api/v1/sda/multicast/virtualNetworks` | getMulticastVirtualNetworks | Get multicast virtual networks | Query: fabricId, virtualNetworkName, offset, limit |
| PUT | `/dna/intent/api/v1/sda/multicast/virtualNetworks` | updateMulticastVirtualNetworks | Update multicast virtual networks |  |
| GET | `/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/count` | getFabricDevicesLayer2HandoffsCount | Get fabric devices layer 2 handoffs count | Query: fabricId, networkDeviceId |
| GET | `/dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness` | sdaFabricSitesReadiness | Sda Fabric Sites Readiness | Query: order, sortBy |
| DELETE | `/dna/intent/api/v1/sda/multicast/virtualNetworks/{id}` | deleteMulticastVirtualNetworkById | Delete multicast virtual network by id | id |
| GET | `/dna/intent/api/v1/sda/fabricSites/count` | getFabricSiteCount | Get fabric site count |  |
| PUT | `/dna/intent/api/v1/sda/anycastGateways` | updateAnycastGateways | Update anycast gateways |  |
| GET | `/dna/intent/api/v1/sda/anycastGateways` | getAnycastGateways | Get anycast gateways | Query: id, fabricId, virtualNetworkName, ipPoolName, vlanName, vlanId, offset, limit |
| POST | `/dna/intent/api/v1/sda/anycastGateways` | addAnycastGateways | Add anycast gateways |  |
| POST | `/dna/intent/api/v1/sda/extranetPolicies` | addExtranetPolicy | Add extranet policy |  |
| GET | `/dna/intent/api/v1/sda/extranetPolicies` | getExtranetPolicies | Get extranet policies | Query: extranetPolicyName, offset, limit |
| PUT | `/dna/intent/api/v1/sda/extranetPolicies` | updateExtranetPolicy | Update extranet policy |  |
| DELETE | `/dna/intent/api/v1/sda/extranetPolicies` | deleteExtranetPolicies | Delete extranet policies | Query: extranetPolicyName |
| GET | `/dna/intent/api/v1/sda/fabricZones/count` | getFabricZoneCount | Get fabric zone count |  |
| GET | `/dna/intent/api/v1/securityServiceInsertionSummaries` | securityServiceInsertionSummary | Security Service Insertion Summary | Query: order, limit, offset, fabricSiteName |
| PUT | `/dna/intent/api/v1/sda/layer2VirtualNetworks` | updateLayer2VirtualNetworks | Update layer 2 virtual networks |  |
| GET | `/dna/intent/api/v1/sda/layer2VirtualNetworks` | getLayer2VirtualNetworks | Get layer 2 virtual networks | Query: id, fabricId, vlanName, vlanId, trafficType, associatedLayer3VirtualNetworkName, offset, limit |
| DELETE | `/dna/intent/api/v1/sda/layer2VirtualNetworks` | deleteLayer2VirtualNetworks | Delete layer 2 virtual networks | Query: fabricId, vlanName, vlanId, trafficType, associatedLayer3VirtualNetworkName |
| POST | `/dna/intent/api/v1/sda/layer2VirtualNetworks` | addLayer2VirtualNetworks | Add layer 2 virtual networks |  |
| GET | `/dna/data/api/v1/transitNetworkHealthSummaries/{id}/trendAnalytics` | theTrendAnalyticsDataForATransitNetworkInTheSpecifiedTimeRange | The Trend analytics data for a transit network in the specified time range | id | Query: startTime, endTime, trendInterval, limit, offset, order, attribute |
| GET | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits` | getFabricDevicesLayer3HandoffsWithSdaTransit | Get fabric devices layer 3 handoffs with sda transit | Query: fabricId, networkDeviceId, offset, limit |
| POST | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits` | addFabricDevicesLayer3HandoffsWithSdaTransit | Add fabric devices layer 3 handoffs with sda transit |  |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits` | deleteFabricDeviceLayer3HandoffsWithSdaTransit | Delete fabric device layer 3 handoffs with sda transit | Query: fabricId, networkDeviceId |
| PUT | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits` | updateFabricDevicesLayer3HandoffsWithSdaTransit | Update fabric devices layer 3 handoffs with sda transit |  |
| POST | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits` | addFabricDevicesLayer3HandoffsWithIpTransit | Add fabric devices layer 3 handoffs with ip transit |  |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits` | deleteFabricDeviceLayer3HandoffsWithIpTransit | Delete fabric device layer 3 handoffs with ip transit | Query: fabricId, networkDeviceId |
| GET | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits` | getFabricDevicesLayer3HandoffsWithIpTransit | Get fabric devices layer 3 handoffs with ip transit | Query: fabricId, networkDeviceId, offset, limit |
| PUT | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits` | updateFabricDevicesLayer3HandoffsWithIpTransit | Update fabric devices layer 3 handoffs with ip transit |  |
| GET | `/dna/data/api/v1/fabricSiteHealthSummaries` | readListOfFabricSitesWithTheirHealthSummary | Read list of Fabric Sites with their health summary | Query: startTime, endTime, limit, offset, sortBy, order, id, attribute, view, siteHierarchy, siteHierarchyId |
| GET | `/dna/data/api/v1/transitNetworkHealthSummaries/{id}` | readTransitNetworkWithItsHealthSummaryFromId | Read transit network with its health summary from id | id | Query: endTime, startTime, attribute, view |
| GET | `/dna/intent/api/v1/sda/layer3VirtualNetworks` | getLayer3VirtualNetworks | Get layer 3 virtual networks | Query: virtualNetworkName, fabricId, anchoredSiteId, offset, limit |
| DELETE | `/dna/intent/api/v1/sda/layer3VirtualNetworks` | deleteLayer3VirtualNetworks | Delete layer 3 virtual networks | Query: virtualNetworkName |
| POST | `/dna/intent/api/v1/sda/layer3VirtualNetworks` | addLayer3VirtualNetworks | Add layer 3 virtual networks |  |
| PUT | `/dna/intent/api/v1/sda/layer3VirtualNetworks` | updateLayer3VirtualNetworks | Update layer 3 virtual networks |  |
| POST | `/dna/intent/api/v1/sda/portChannels` | addPortChannels | Add port channels |  |
| GET | `/dna/intent/api/v1/sda/portChannels` | getPortChannels-2 | Get port channels | Query: fabricId, networkDeviceId, portChannelName, connectedDeviceType, offset, limit |
| PUT | `/dna/intent/api/v1/sda/portChannels` | updatePortChannels | Update port channels |  |
| DELETE | `/dna/intent/api/v1/sda/portChannels` | deletePortChannels | Delete port channels | Query: fabricId, networkDeviceId, portChannelName, portChannelIds, connectedDeviceType |
| GET | `/dna/intent/api/v1/sda/extranetPolicies/count` | getExtranetPolicyCount | Get extranet policy count |  |
| GET | `/dna/data/api/v1/virtualNetworkHealthSummaries/{id}` | readVirtualNetworkWithItsHealthSummaryFromId | Read virtual network with its health summary from id | id | Query: endTime, startTime, attribute, view |
| GET | `/dna/intent/api/v1/securityServiceInsertion/systemReadiness` | securityServiceInsertionReadiness | Security Service Insertion Readiness |  |
| GET | `/dna/intent/api/v1/sda/portAssignments/count` | getPortAssignmentCount | Get port assignment count | Query: fabricId, networkDeviceId, interfaceName, dataVlanName, voiceVlanName |
| GET | `/dna/intent/api/v1/sda/pendingFabricEvents` | getPendingFabricEvents | Get pending fabric events | Query: fabricId, offset, limit |
| DELETE | `/dna/intent/api/v1/sda/extranetPolicies/{id}` | deleteExtranetPolicyById | Delete extranet policy by id | id |
| GET | `/dna/data/api/v1/transitNetworkHealthSummaries` | readListOfTransitNetworksWithTheirHealthSummary | Read list of Transit Networks with their health summary | Query: startTime, endTime, limit, offset, sortBy, order, id, attribute, view |
| DELETE | `/dna/intent/api/v1/sda/anycastGateways/{id}` | deleteAnycastGatewayById | Delete anycast gateway by id | id |
| DELETE | `/dna/intent/api/v1/sda/provisionDevices` | deleteProvisionedDevices | Delete provisioned devices | Query: networkDeviceId, siteId, cleanUpConfig |
| PUT | `/dna/intent/api/v1/sda/provisionDevices` | re-provisionDevices | Re-provision devices |  |
| POST | `/dna/intent/api/v1/sda/provisionDevices` | provisionDevices | Provision devices |  |
| GET | `/dna/intent/api/v1/sda/provisionDevices` | getProvisionedDevices | Get provisioned devices | Query: id, networkDeviceId, siteId, offset, limit |
| DELETE | `/dna/intent/api/v1/sda/layer3VirtualNetworks/{id}` | deleteLayer3VirtualNetworkById | Delete layer 3 virtual network by id | id |
| DELETE | `/dna/intent/api/v1/securityServiceInsertions/{id}` | deleteSecurityServiceInsertion | Delete Security Service Insertion | id |
| PUT | `/dna/intent/api/v1/securityServiceInsertions/{id}` | updateTheSecurityServiceInsertion. | Update the Security Service Insertion. | id |
| GET | `/dna/intent/api/v1/securityServiceInsertions/{id}` | securityServiceInsertionById. | Security Service Insertion by Id. | id |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/{id}` | deleteFabricDeviceLayer2HandoffById | Delete fabric device layer 2 handoff by id | id |
| DELETE | `/dna/intent/api/v1/sda/portChannels/{id}` | deletePortChannelById | Delete port channel by id | id |
| GET | `/dna/data/api/v1/transitNetworkHealthSummaries/count` | readTransitNetworksCount | Read Transit Networks count | Query: startTime, endTime, id |
| POST | `/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs` | addFabricDevicesLayer2Handoffs | Add fabric devices layer 2 handoffs |  |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs` | deleteFabricDeviceLayer2Handoffs | Delete fabric device layer 2 handoffs | Query: fabricId, networkDeviceId |
| GET | `/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs` | getFabricDevicesLayer2Handoffs | Get fabric devices layer 2 handoffs | Query: fabricId, networkDeviceId, offset, limit |
| GET | `/dna/intent/api/v1/sda/layer2VirtualNetworks/count` | getLayer2VirtualNetworkCount | Get layer 2 virtual network count | Query: fabricId, vlanName, vlanId, trafficType, associatedLayer3VirtualNetworkName |
| POST | `/dna/intent/api/v1/sda/fabricDevices` | addFabricDevices | Add fabric devices |  |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices` | deleteFabricDevices | Delete fabric devices | Query: fabricId, networkDeviceId, deviceRoles |
| PUT | `/dna/intent/api/v1/sda/fabricDevices` | updateFabricDevices | Update fabric devices |  |
| GET | `/dna/intent/api/v1/sda/fabricDevices` | getFabricDevices | Get fabric devices | Query: fabricId, networkDeviceId, deviceRoles, offset, limit |
| PUT | `/dna/intent/api/v1/sda/transitNetworks` | updateTransitNetworks | Update transit networks |  |
| POST | `/dna/intent/api/v1/sda/transitNetworks` | addTransitNetworks | Add transit networks |  |
| GET | `/dna/intent/api/v1/sda/transitNetworks` | getTransitNetworks | Get transit networks | Query: id, name, type, offset, limit |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices/{id}` | deleteFabricDeviceById | Delete fabric device by id | id |
| POST | `/dna/intent/api/v1/sda/fabricZones` | addFabricZone | Add fabric zone |  |
| GET | `/dna/intent/api/v1/sda/fabricZones` | getFabricZones | Get fabric zones | Query: id, siteId, offset, limit |
| PUT | `/dna/intent/api/v1/sda/fabricZones` | updateFabricZone | Update fabric zone |  |
| GET | `/dna/data/api/v1/fabricSiteHealthSummaries/{id}/trendAnalytics` | theTrendAnalyticsDataForAFabricSiteInTheSpecifiedTimeRange | The Trend analytics data for a fabric site in the specified time range | id | Query: startTime, endTime, trendInterval, limit, offset, order, attribute |
| GET | `/dna/intent/api/v1/sda/multicast/virtualNetworks/count` | getMulticastVirtualNetworkCount | Get multicast virtual network count | Query: fabricId |
| PUT | `/dna/intent/api/v1/sda/authenticationProfiles` | updateAuthenticationProfile | Update authentication profile |  |
| GET | `/dna/intent/api/v1/sda/authenticationProfiles` | getAuthenticationProfiles | Get authentication profiles | Query: fabricId, authenticationProfileName, isGlobalAuthenticationProfile, offset, limit |
| DELETE | `/dna/intent/api/v1/sda/fabricZones/{id}` | deleteFabricZoneById | Delete fabric zone by id | id |
| GET | `/dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness/{id}` | readinessStatusForAFabricSite. | Readiness status for a fabric site. | id | Query: order |
| POST | `/dna/intent/api/v1/sda/pendingFabricEvents/apply` | applyPendingFabricEvents | Apply pending fabric events |  |
| GET | `/dna/intent/api/v1/securityServiceInsertionSummaries/count` | countOfSecurityServiceInsertionSummaries. | Count of Security Service Insertion summaries. |  |
| GET | `/dna/intent/api/v1/sda/portChannels/count` | getPortChannelCount | Get port channel count | Query: fabricId, networkDeviceId, portChannelName, connectedDeviceType |
| POST | `/dna/intent/api/v1/sda/fabricSites` | addFabricSite | Add fabric site |  |
| PUT | `/dna/intent/api/v1/sda/fabricSites` | updateFabricSite | Update fabric site |  |
| GET | `/dna/intent/api/v1/sda/fabricSites` | getFabricSites | Get fabric sites | Query: id, siteId, offset, limit |
| GET | `/dna/intent/api/v1/sda/layer3VirtualNetworks/count` | getLayer3VirtualNetworksCount | Get layer 3 virtual networks count | Query: fabricId, anchoredSiteId |
| GET | `/dna/intent/api/v1/sda/fabricDevices/count` | getFabricDevicesCount | Get fabric devices count | Query: fabricId, networkDeviceId, deviceRoles |
| DELETE | `/dna/intent/api/v1/sda/provisionDevices/{id}` | deleteProvisionedDeviceById | Delete provisioned device by Id | id | Query: cleanUpConfig |
| DELETE | `/dna/intent/api/v1/sda/transitNetworks/{id}` | deleteTransitNetworkById | Delete transit network by id | id |
| GET | `/dna/intent/api/v1/sda/transitNetworks/count` | getTransitNetworksCount | Get transit networks count | Query: type |
| GET | `/dna/data/api/v1/virtualNetworkHealthSummaries` | readListOfVirtualNetworksWithTheirHealthSummary | Read list of Virtual Networks with their health summary | Query: startTime, endTime, limit, offset, sortBy, order, id, vnLayer, attribute, view, siteHierarchy, SiteHierarchyId |
| GET | `/dna/intent/api/v1/securityServiceInsertions/count` | countOfSecurityServiceInsertions. | Count of Security Service Insertions. |  |
| PUT | `/dna/intent/api/v1/sda/multicast` | updateMulticast | Update multicast |  |
| GET | `/dna/intent/api/v1/sda/multicast` | getMulticast | Get multicast | Query: fabricId, offset, limit |
| GET | `/dna/data/api/v1/virtualNetworkHealthSummaries/count` | readVirtualNetworksCount | Read Virtual Networks count | Query: startTime, endTime, id, vnLayer, siteHierarchy, siteHierarchyId |
| DELETE | `/dna/intent/api/v1/sda/fabricSites/{id}` | deleteFabricSiteById | Delete fabric site by id | id |
| DELETE | `/dna/intent/api/v1/sda/layer2VirtualNetworks/{id}` | deleteLayer2VirtualNetworkById | Delete layer 2 virtual network by id | id |
| GET | `/dna/data/api/v1/virtualNetworkHealthSummaries/{id}/trendAnalytics` | theTrendAnalyticsDataForAVirtualNetworkInTheSpecifiedTimeRange | The Trend analytics data for a virtual network in the specified time range | id | Query: startTime, endTime, trendInterval, limit, offset, order, attribute |
| GET | `/dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness/{siteId}/virtualNetworks/{id}` | readinessStatusOfSwitchesInASpecifiedVirtualNetworkWithinAFabricSite. | Readiness status of switches in a specified virtual network within a fabric site. | siteId, id |
| DELETE | `/dna/intent/api/v1/sda/portAssignments` | deletePortAssignments | Delete port assignments | Query: fabricId, networkDeviceId, interfaceName, dataVlanName, voiceVlanName |
| GET | `/dna/intent/api/v1/sda/portAssignments` | getPortAssignments | Get port assignments | Query: fabricId, networkDeviceId, interfaceName, dataVlanName, voiceVlanName, offset, limit |
| POST | `/dna/intent/api/v1/sda/portAssignments` | addPortAssignments | Add port assignments |  |
| PUT | `/dna/intent/api/v1/sda/portAssignments` | updatePortAssignments | Update port assignments |  |
| GET | `/dna/data/api/v1/fabricSiteHealthSummaries/count` | readFabricSiteCount | Read fabric site count | Query: startTime, endTime, id, siteHierarchy, siteHierarchyId |
| GET | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits/count` | getFabricDevicesLayer3HandoffsWithIpTransitCount | Get fabric devices layer 3 handoffs with ip transit count | Query: fabricId, networkDeviceId |
| GET | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaTransits/count` | getFabricDevicesLayer3HandoffsWithSdaTransitCount | Get fabric devices layer 3 handoffs with sda transit count | Query: fabricId, networkDeviceId |
| DELETE | `/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTransits/{id}` | deleteFabricDeviceLayer3HandoffWithIpTransitById | Delete fabric device layer 3 handoff with ip transit by id | id |
| POST | `/dna/intent/api/v1/securityServiceInsertions` | createSecurityServiceInsertionOnASpecificFabricSite. | Create security service insertion on a specific fabric site. |  |
| GET | `/dna/intent/api/v1/securityServiceInsertions` | securityServiceInsertions. | Security Service Insertions. | Query: limit, offset, order, name |
| GET | `/dna/data/api/v1/fabricSummary` | readFabricEntitySummary | Read Fabric entity summary | Query: startTime, endTime, siteHierarchy, siteHierarchyId |
| GET | `/dna/intent/api/v1/sda/anycastGateways/count` | getAnycastGatewayCount | Get anycast gateway count | Query: fabricId, virtualNetworkName, ipPoolName, vlanName, vlanId |
| GET | `/dna/intent/api/v1/sda/provisionDevices/count` | getProvisionedDevicesCount | Get Provisioned Devices count | Query: siteId |
| GET | `/dna/data/api/v1/fabricSiteHealthSummaries/{id}` | readFabricSitesWithHealthSummaryFromId | Read Fabric Sites with health summary from id | id | Query: startTime, endTime, attribute, view |
| DELETE | `/dna/intent/api/v1/sda/portAssignments/{id}` | deletePortAssignmentById | Delete port assignment by id | id |
| DELETE | `/dna/intent/api/v1/business/sda/hostonboarding/access-point` | deletePortAssignmentForAccessPointInSDAFabric | Delete Port assignment for access point in SDA Fabric | Query: deviceManagementIpAddress, interfaceName |
| GET | `/dna/intent/api/v1/business/sda/hostonboarding/access-point` | getPortAssignmentForAccessPointInSDAFabric | Get Port assignment for access point in SDA Fabric | Query: deviceManagementIpAddress, interfaceName |
| POST | `/dna/intent/api/v1/business/sda/hostonboarding/access-point` | addPortAssignmentForAccessPointInSDAFabric | Add Port assignment for access point in SDA Fabric |  |
| DELETE | `/dna/intent/api/v1/business/sda/edge-device` | deleteEdgeDeviceFromSDAFabric | Delete edge device from SDA Fabric | Query: deviceManagementIpAddress |
| GET | `/dna/intent/api/v1/business/sda/edge-device` | getEdgeDeviceFromSDAFabric | Get edge device from SDA Fabric | Query: deviceManagementIpAddress |
| POST | `/dna/intent/api/v1/business/sda/edge-device` | addEdgeDeviceInSDAFabric | Add edge device in SDA Fabric |  |
| GET | `/dna/intent/api/v1/business/sda/device` | getDeviceInfoFromSDAFabric | Get device info from SDA Fabric | Query: deviceManagementIpAddress |
| POST | `/dna/intent/api/v1/business/sda/virtualnetwork/ippool` | addIPPoolInSDAVirtualNetwork | Add IP Pool in SDA Virtual Network |  |
| DELETE | `/dna/intent/api/v1/business/sda/virtualnetwork/ippool` | deleteIPPoolFromSDAVirtualNetwork | Delete IP Pool from SDA Virtual Network | Query: siteNameHierarchy, virtualNetworkName, ipPoolName |
| GET | `/dna/intent/api/v1/business/sda/virtualnetwork/ippool` | getIPPoolFromSDAVirtualNetwork | Get IP Pool from SDA Virtual Network | Query: siteNameHierarchy, virtualNetworkName, ipPoolName |
| DELETE | `/dna/intent/api/v1/business/sda/fabric-site` | deleteSiteFromSDAFabric | Delete Site from SDA Fabric | Query: siteNameHierarchy |
| GET | `/dna/intent/api/v1/business/sda/fabric-site` | getSiteFromSDAFabric | Get Site from SDA Fabric | Query: siteNameHierarchy |
| POST | `/dna/intent/api/v1/business/sda/fabric-site` | addSiteInSDAFabric | Add Site in SDA Fabric |  |
| DELETE | `/dna/intent/api/v1/business/sda/authentication-profile` | deleteDefaultAuthenticationProfileFromSDAFabric | Delete default authentication profile from SDA Fabric | Query: siteNameHierarchy |
| POST | `/dna/intent/api/v1/business/sda/authentication-profile` | addDefaultAuthenticationTemplateInSDAFabric | Add default authentication template in SDA Fabric |  |
| PUT | `/dna/intent/api/v1/business/sda/authentication-profile` | updateDefaultAuthenticationProfileInSDAFabric | Update default authentication profile in SDA Fabric |  |
| GET | `/dna/intent/api/v1/business/sda/authentication-profile` | getDefaultAuthenticationProfileFromSDAFabric | Get default authentication profile from SDA Fabric | Query: siteNameHierarchy, authenticateTemplateName |
| DELETE | `/dna/intent/api/v1/business/sda/multicast` | deleteMulticastFromSDAFabric | Delete multicast from SDA fabric | Query: siteNameHierarchy |
| GET | `/dna/intent/api/v1/business/sda/multicast` | getMulticastDetailsFromSDAFabric | Get multicast details from SDA fabric | Query: siteNameHierarchy |
| POST | `/dna/intent/api/v1/business/sda/multicast` | addMulticastInSDAFabric | Add multicast in SDA fabric |  |
| POST | `/dna/intent/api/v1/business/sda/virtual-network` | addVNInFabric | Add VN in fabric |  |
| GET | `/dna/intent/api/v1/business/sda/virtual-network` | getVNFromSDAFabric | Get VN from SDA Fabric | Query: virtualNetworkName, siteNameHierarchy |
| DELETE | `/dna/intent/api/v1/business/sda/virtual-network` | deleteVNFromSDAFabric | Delete VN from SDA Fabric | Query: virtualNetworkName, siteNameHierarchy |
| PUT | `/dna/intent/api/v1/business/sda/provision-device` | re-ProvisionWiredDevice | Re-Provision Wired Device |  |
| POST | `/dna/intent/api/v1/business/sda/provision-device` | provisionWiredDevice | Provision Wired Device |  |
| DELETE | `/dna/intent/api/v1/business/sda/provision-device` | deleteProvisionedWiredDevice | Delete provisioned Wired Device | Query: deviceManagementIpAddress |
| GET | `/dna/intent/api/v1/business/sda/provision-device` | getProvisionedWiredDevice | Get Provisioned Wired Device | Query: deviceManagementIpAddress |
| GET | `/dna/intent/api/v1/business/sda/virtual-network/summary` | getVirtualNetworkSummary | Get Virtual Network Summary | Query: siteNameHierarchy |
| POST | `/dna/intent/api/v1/business/sda/hostonboarding/user-device` | addPortAssignmentForUserDeviceInSDAFabric | Add Port assignment for user device in SDA Fabric |  |
| DELETE | `/dna/intent/api/v1/business/sda/hostonboarding/user-device` | deletePortAssignmentForUserDeviceInSDAFabric | Delete Port assignment for user device in SDA Fabric | Query: deviceManagementIpAddress, interfaceName |
| GET | `/dna/intent/api/v1/business/sda/hostonboarding/user-device` | getPortAssignmentForUserDeviceInSDAFabric | Get Port assignment for user device in SDA Fabric | Query: deviceManagementIpAddress, interfaceName |
| GET | `/dna/intent/api/v1/business/sda/transit-peer-network` | getTransitPeerNetworkInfo | Get Transit Peer Network Info | Query: transitPeerNetworkName |
| POST | `/dna/intent/api/v1/business/sda/transit-peer-network` | addTransitPeerNetwork | Add Transit Peer Network |  |
| DELETE | `/dna/intent/api/v1/business/sda/transit-peer-network` | deleteTransitPeerNetwork | Delete Transit Peer Network | Query: transitPeerNetworkName |
| PUT | `/dna/intent/api/v1/virtual-network` | updateVirtualNetworkWithScalableGroups | Update virtual network with scalable groups |  |
| DELETE | `/dna/intent/api/v1/virtual-network` | deleteVirtualNetworkWithScalableGroups | Delete virtual network with scalable groups | Query: virtualNetworkName |
| GET | `/dna/intent/api/v1/virtual-network` | getVirtualNetworkWithScalableGroups | Get virtual network with scalable groups | Query: virtualNetworkName |
| POST | `/dna/intent/api/v1/virtual-network` | addVirtualNetworkWithScalableGroups | Add virtual network with scalable groups |  |
| DELETE | `/dna/intent/api/v1/business/sda/border-device` | deleteBorderDeviceFromSDAFabric | Delete border device from SDA Fabric | Query: deviceManagementIpAddress |
| GET | `/dna/intent/api/v1/business/sda/border-device` | getBorderDeviceDetailFromSDAFabric | Get border device detail from SDA Fabric | Query: deviceManagementIpAddress |
| POST | `/dna/intent/api/v1/business/sda/border-device` | addBorderDeviceInSDAFabric | Add border device in SDA Fabric |  |
| GET | `/dna/intent/api/v1/business/sda/device/role` | getDeviceRoleInSDAFabric | Get device role in SDA Fabric | Query: deviceManagementIpAddress |
| GET | `/dna/intent/api/v1/business/sda/control-plane-device` | getControlPlaneDeviceFromSDAFabric | Get control plane device from SDA Fabric | Query: deviceManagementIpAddress |
| POST | `/dna/intent/api/v1/business/sda/control-plane-device` | addControlPlaneDeviceInSDAFabric | Add control plane device in SDA Fabric |  |
| DELETE | `/dna/intent/api/v1/business/sda/control-plane-device` | deleteControlPlaneDeviceInSDAFabric | Delete control plane device in SDA Fabric | Query: deviceManagementIpAddress |

#### Wired

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels` | createAConfigurationModelForTheIntendedConfigsForADevice. | Create a configuration model for the intended configs for a device. | networkDeviceId |
| PUT | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}` | updateConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice. | Update configurations for an intended layer 2 feature on a wired device. | id, feature |
| GET | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}` | getConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice. | Get configurations for an intended layer 2 feature on a wired device. | id, feature |
| POST | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}` | createConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice | Create configurations for an intended layer 2 feature on a wired device | id, feature |
| DELETE | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}` | deleteConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice. | Delete configurations for an intended layer 2 feature on a wired device. | id, feature |
| GET | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/deployed/layer2/{feature}/count` | getNumberOfConfigurationsForADeployedLayer2FeatureOnADevice. | Get number of configurations for a deployed layer 2 feature on a device. | id, feature |
| GET | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/deployed/layer2/{feature}` | getConfigurationsForADeployedLayer2FeatureOnAWiredDevice. | Get configurations for a deployed layer 2 feature on a wired device. | id, feature |
| POST | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/deploy` | deployTheIntendedConfigurationFeaturesOnAWiredDevice. | Deploy the intended configuration features on a wired device. | networkDeviceId |
| GET | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/serviceDeployments` | getServiceDeploymentStatus. | Get service deployment status. | networkDeviceId |
| PUT | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2` | updateConfigurationsForIntendedLayer2FeaturesOnAWiredDevice. | Update configurations for intended layer 2 features on a wired device. | id |
| POST | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2` | createConfigurationsForIntendedLayer2FeaturesOnAWiredDevice | Create configurations for intended layer 2 features on a wired device | id |
| GET | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/supported/layer2` | getTheSupportedLayer2FeaturesOnAWiredDevice. | Get the supported layer 2 features on a wired device. | id |
| POST | `/dna/intent/api/v1/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}/deploy` | deploysTheConfigurationModelOnTheNetworkDevice. | Deploys the configuration model on the network device. | networkDeviceId, previewActivityId |
| GET | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}/count` | getNumberOfConfigurationsForAnIntendedLayer2FeatureOnADevice. | Get number of configurations for an intended layer 2 feature on a device. | id, feature |
| POST | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}/config` | generateTheDeviceConfigForTheConfigurationModel. | Generate the device config for the configuration model. | networkDeviceId, previewActivityId |
| GET | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}/config` | getsTheDeviceConfigForTheConfigurationModel. | Gets the device config for the configuration model. | networkDeviceId, previewActivityId |
| DELETE | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}` | deletesTheConfigurationModel. | Deletes the configuration model. | networkDeviceId, previewActivityId |
| GET | `/dna/intent/api/v1/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2` | getConfigurationsForIntendedLayer2FeaturesOnAWiredDevice. | Get configurations for intended layer 2 features on a wired device. | id | Query: feature |
| GET | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/deviceDeployments` | getDeviceDeploymentStatus | Get device deployment status | networkDeviceId |

#### Wireless

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/wireless/accesspoint-configuration` | configureAccessPointsV1 | Configure Access Points V1 |  |
| GET | `/dna/intent/api/v1/wirelessSettings/apAuthorizationLists/{id}` | getAPAuthorizationListByID | Get AP Authorization List by ID | id |
| PUT | `/dna/intent/api/v1/wirelessSettings/apAuthorizationLists/{id}` | updateAPAuthorizationList | Update AP Authorization List | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/apAuthorizationLists/{id}` | deleteAPAuthorizationList | Delete AP Authorization List | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/interfaces/{id}` | deleteInterface | Delete Interface | id |
| PUT | `/dna/intent/api/v1/wirelessSettings/interfaces/{id}` | updateInterface | Update Interface | id |
| GET | `/dna/intent/api/v1/wirelessSettings/interfaces/{id}` | getInterfaceByID | Get Interface by ID | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/powerProfiles/{id}` | deletePowerProfileByID | Delete Power Profile by ID | id |
| GET | `/dna/intent/api/v1/wirelessSettings/powerProfiles/{id}` | getPowerProfileByID | Get Power Profile by ID | id |
| PUT | `/dna/intent/api/v1/wirelessSettings/powerProfiles/{id}` | updatePowerProfileByID | Update Power Profile by ID | id |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/eventDrivenRRMConfigurations` | createEventDrivenRRMConfigurationFeatureTemplate | Create Event Driven RRM Configuration Feature Template |  |
| GET | `/dna/intent/api/v1/wirelessSettings/rfProfiles` | getRFProfiles | Get RF Profiles | Query: limit, offset, rfProfileName, enableRadioTypeA, enableRadioTypeB, enableRadioType6GHz |
| POST | `/dna/intent/api/v1/wirelessSettings/rfProfiles` | createRFProfile | Create RF Profile |  |
| POST | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids` | createSSID | Create SSID | siteId |
| GET | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids` | getSSIDBySite | Get SSID by Site | siteId | Query: limit, offset, ssid, wlanType, authType, l3authType |
| GET | `/dna/intent/api/v1/wirelessSettings/anchorGroups/{id}` | getAnchorGroupByID | Get AnchorGroup by ID | id |
| PUT | `/dna/intent/api/v1/wirelessSettings/anchorGroups/{id}` | updateAnchorGroup | Update AnchorGroup | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/anchorGroups/{id}` | deleteAnchorGroupByID | Delete AnchorGroup by ID | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/flexConnectConfigurations/{id}` | updateFlexConnectConfigurationFeatureTemplate | Update Flex Connect Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/flexConnectConfigurations/{id}` | deleteFlexConnectConfigurationFeatureTemplate | Delete Flex Connect Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/flexConnectConfigurations/{id}` | getFlexConnectConfigurationFeatureTemplate | Get Flex Connect Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/wireless/accesspoint-configuration/count` | getAccessPointConfigurationCount | Get Access Point Configuration Count | Query: wlcIpAddress, apMode, apModel, meshRole, provisioned |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId}` | retrieveASpecificSiteTagForAWirelessProfile | Retrieve a specific Site Tag for a Wireless Profile | id, siteTagId |
| PUT | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId}` | updateASpecificSiteTagForAWirelessProfile | Update a specific Site Tag for a Wireless Profile | id, siteTagId |
| DELETE | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId}` | deleteASpecificSiteTagFromAWirelessProfile | Delete a specific Site Tag from a Wireless Profile | id, siteTagId |
| DELETE | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectNativeVlan` | deleteNativeVlanSettingsBySite | Delete Native Vlan Settings By Site | siteId | Query: removeOverrideInHierarchy |
| PUT | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectNativeVlan` | updateNativeVlanSettingsBySite | Update Native Vlan Settings  By Site | siteId |
| GET | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectNativeVlan` | getNativeVlanSettingsBySite | Get Native Vlan Settings By Site | siteId |
| PUT | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id}` | updateSSID | Update SSID | siteId, id |
| GET | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id}` | getSSIDByID | Get SSID by ID | siteId, id |
| DELETE | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id}` | deleteSSID | Delete SSID | siteId, id | Query: removeOverrideInHierarchy |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfigurations/{id}` | getRRMFRAConfigurationFeatureTemplate | Get RRM FRA Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfigurations/{id}` | updateRRMFRAConfigurationFeatureTemplate | Update RRM FRA Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfigurations/{id}` | deleteRRMFRAConfigurationFeatureTemplate | Delete RRM FRA Configuration Feature Template | id |
| POST | `/dna/intent/api/v1/wirelessAccessPoints/provision` | aPProvision | AP Provision |  |
| GET | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectAaaOverride` | getAAAOverrideVlanSettingsBySite | Get AAA Override Vlan Settings By Site | siteId |
| PUT | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectAaaOverride` | updateAAAOverrideVlanSettingsBySite | Update AAA Override Vlan Settings By Site | siteId |
| DELETE | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectAaaOverride` | deleteAAAOverrideVlanSettingsBySite | Delete AAA Override Vlan Settings By Site | siteId | Query: removeOverrideInHierarchy |
| GET | `/dna/intent/api/v1/wirelessSettings/dot11beProfiles` | get802.11beProfiles | Get 802.11be Profiles | Query: limit, offset, profileName, isOfDmaDownLink, isOfDmaUpLink, isMuMimoUpLink, isMuMimoDownLink, isOfDmaMultiRu |
| POST | `/dna/intent/api/v1/wirelessSettings/dot11beProfiles` | createA802.11beProfile | Create a 802.11be Profile |  |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/summary` | getFeatureTemplateSummary | Get Feature Template Summary | Query: type, designName, limit, offset, systemTemplate |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/count` | retrieveTheCountOfPolicyTagsForAWirelessProfile | Retrieve the count of Policy Tags for a Wireless Profile | id |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/primaryManagedApLocations` | getPrimaryManagedAPLocationsForSpecificWirelessController | Get Primary Managed AP Locations for specific Wireless Controller | networkDeviceId | Query: limit, offset |
| PUT | `/dna/intent/api/v1/systemSettings/apPnPLocation` | updateAPPnPLocationSetting | Update AP PnP Location Setting |  |
| GET | `/dna/intent/api/v1/systemSettings/apPnPLocation` | getAPPnPLocationSetting | Get AP PnP Location Setting |  |
| DELETE | `/dna/intent/api/v1/wirelessProfiles/{id}` | deleteWirelessProfile | Delete Wireless Profile | id |
| PUT | `/dna/intent/api/v1/wirelessProfiles/{id}` | updateWirelessProfile | Update Wireless Profile | id |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}` | getWirelessProfileByID | Get Wireless Profile by ID | id |
| GET | `/dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/count` | getMobilityGroupsCount | Get MobilityGroups Count |  |
| PUT | `/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}` | updateRFProfile | Update RF Profile | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}` | deleteRFProfile | Delete RF Profile | id |
| GET | `/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}` | getRFProfileByID | Get RF Profile by ID | id |
| GET | `/dna/intent/api/v1/wirelessSettings/anchorGroups` | getAnchorGroups | Get AnchorGroups |  |
| POST | `/dna/intent/api/v1/wirelessSettings/anchorGroups` | createAnchorGroup | Create AnchorGroup |  |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations/{id}` | getAAARadiusAttributesConfigurationFeatureTemplate | Get AAA Radius Attributes Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations/{id}` | updateAAARadiusAttributesConfigurationFeatureTemplate | Update AAA Radius Attributes Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations/{id}` | deleteAAARadiusAttributesConfigurationFeatureTemplate | Delete AAA Radius Attributes Configuration Feature Template | id |
| POST | `/dna/intent/api/v1/wirelessSettings/apProfiles` | createAPProfile | Create AP Profile |  |
| GET | `/dna/intent/api/v1/wirelessSettings/apProfiles` | getAPProfiles | Get AP Profiles | Query: limit, offset, apProfileName |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/ssidDetails/count` | getSSIDCountForSpecificWirelessController | Get SSID Count for specific Wireless Controller | networkDeviceId | Query: adminStatus, managed |
| PUT | `/dna/intent/api/v1/wirelessSettings/apProfiles/{id}` | updateAPProfileByID | Update AP Profile by ID | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/apProfiles/{id}` | deleteAPProfileByID | Delete AP Profile by ID | id |
| GET | `/dna/intent/api/v1/wirelessSettings/apProfiles/{id}` | getAPProfileByID | Get AP Profile by ID | id |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags` | retrieveAllPolicyTagsForAWirelessProfile | Retrieve all Policy Tags for a Wireless Profile | id | Query: limit, offset, policyTagName |
| GET | `/dna/intent/api/v1/wirelessSettings/interfaces` | getInterfaces | Get Interfaces | Query: limit, offset, interfaceName, vlanId |
| POST | `/dna/intent/api/v1/wirelessSettings/interfaces` | createInterface | Create Interface |  |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/advancedSSIDConfigurations/{id}` | updateAdvancedSSIDConfigurationFeatureTemplate | Update Advanced SSID Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/advancedSSIDConfigurations/{id}` | deleteAdvancedSSIDConfigurationFeatureTemplate | Delete Advanced SSID Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/advancedSSIDConfigurations/{id}` | getAdvancedSSIDConfigurationFeatureTemplate | Get Advanced SSID Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequestStatus` | getAccessPoint(s)FactoryResetStatus | Get Access Point(s) Factory Reset status | Query: taskId |
| GET | `/dna/intent/api/v1/wirelessProfiles/count` | getWirelessProfilesCount | Get Wireless Profiles Count |  |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations` | createMulticastConfigurationFeatureTemplate | Create Multicast Configuration Feature Template |  |
| DELETE | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{policyTagId}` | deleteASpecificPolicyTagFromAWirelessProfile | Delete a specific Policy Tag from a Wireless Profile | id, policyTagId |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{policyTagId}` | retrieveASpecificPolicyTagForAWirelessProfile | Retrieve a specific Policy Tag for a Wireless Profile | id, policyTagId |
| PUT | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{policyTagId}` | updateASpecificPolicyTagForAWirelessProfile | Update a specific Policy Tag for a Wireless Profile | id, policyTagId |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/dot11axConfigurations` | createDot11axConfigurationFeatureTemplate | Create Dot11ax Configuration Feature Template |  |
| GET | `/dna/intent/api/v1/wirelessSettings/apAuthorizationLists/count` | getAPAuthorizationListCount | Get AP Authorization List Count |  |
| GET | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/count` | getSSIDCountBySite | Get SSID Count by Site | siteId | Query: _inherited |
| GET | `/dna/intent/api/v1/wirelessSettings/anchorGroups/count` | getCountOfAnchorGroups | Get count of AnchorGroups |  |
| POST | `/dna/intent/api/v1/wirelessSettings/{networkDeviceId}/assignAnchorManagedApLocations` | assignAnchorManagedAPLocationsForWLC | Assign Anchor Managed AP Locations For WLC | networkDeviceId |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations` | createAAARadiusAttributesConfigurationFeatureTemplate | Create AAA Radius Attributes Configuration Feature Template |  |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/cleanAirConfigurations/{id}` | deleteCleanAirConfigurationFeatureTemplate | Delete Clean Air Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/cleanAirConfigurations/{id}` | updateCleanAirConfigurationFeatureTemplate | Update Clean Air Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/cleanAirConfigurations/{id}` | getCleanAirConfigurationFeatureTemplate | Get Clean Air Configuration Feature Template | id |
| POST | `/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id}/update` | updateOrOverrideSSID | Update or Override SSID | siteId, id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/dot11beStatusConfigurations/{id}` | deleteDot11beStatusConfigurationFeatureTemplate | Delete Dot11be Status Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/dot11beStatusConfigurations/{id}` | getDot11beStatusConfigurationFeatureTemplate | Get Dot11be Status Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/dot11beStatusConfigurations/{id}` | updateDot11beStatusConfigurationFeatureTemplate | Update Dot11be Status Configuration Feature Template | id |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/cleanAirConfigurations` | createCleanAirConfigurationFeatureTemplate | Create Clean Air Configuration Feature Template |  |
| GET | `/dna/intent/api/v1/wirelessControllers/meshApNeighbours/count` | getMeshApNeighboursCount | Get Mesh Ap Neighbours Count |  |
| GET | `/dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups` | getMobilityGroups	 | Get MobilityGroups	 | Query: networkDeviceId |
| POST | `/dna/intent/api/v2/wireless/accesspoint-configuration` | configureAccessPointsV2 | Configure Access Points V2 |  |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/eventDrivenRRMConfigurations/{id}` | getEventDrivenRRMConfigurationFeatureTemplate | Get Event Driven RRM Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/eventDrivenRRMConfigurations/{id}` | deleteEventDrivenRRMConfigurationFeatureTemplate | Delete Event Driven RRM Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/eventDrivenRRMConfigurations/{id}` | updateEventDrivenRRMConfigurationFeatureTemplate | Update Event Driven RRM Configuration Feature Template | id |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/dot11beStatusConfigurations` | createDot11beStatusConfigurationFeatureTemplate | Create Dot11be Status Configuration Feature Template |  |
| PUT | `/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}` | update802.11beProfile | Update 802.11be Profile | id |
| DELETE | `/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}` | deleteA802.11beProfile | Delete a 802.11be Profile | id |
| GET | `/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}` | get802.11beProfileByID | Get 802.11be Profile by ID | id |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/advancedSSIDConfigurations` | createAdvancedSSIDConfigurationFeatureTemplate | Create Advanced SSID Configuration Feature Template |  |
| POST | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/bulk` | createMultiplePolicyTagsForAWirelessProfileInBulk | Create multiple Policy Tags for a Wireless Profile in bulk | id |
| POST | `/dna/intent/api/v1/device-reboot/apreboot` | rebootAccessPoints | Reboot Access Points |  |
| POST | `/dna/intent/api/v1/wirelessSettings/apAuthorizationLists` | createAPAuthorizationList | Create AP Authorization List |  |
| GET | `/dna/intent/api/v1/wirelessSettings/apAuthorizationLists` | getAPAuthorizationLists | Get AP Authorization Lists | Query: apAuthorizationListName, offset, limit |
| GET | `/dna/intent/api/v1/wirelessSettings/powerProfiles/count` | getPowerProfilesCount | Get Power Profiles Count |  |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/ssidDetails` | getSSIDDetailsForSpecificWirelessController | Get SSID Details for specific Wireless Controller | networkDeviceId | Query: ssidName, adminStatus, managed, limit, offset |
| POST | `/dna/intent/api/v1/wirelessSettings/powerProfiles` | createPowerProfile | Create Power Profile |  |
| GET | `/dna/intent/api/v1/wirelessSettings/powerProfiles` | getPowerProfiles | Get Power Profiles | Query: limit, offset, profileName |
| POST | `/dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/mobilityProvision` | mobilityProvision | Mobility Provision |  |
| POST | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/bulk` | createMultipleSiteTagsForAWirelessProfileInBulk | Create multiple Site Tags for a Wireless Profile in bulk | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations/{id}` | getMulticastConfigurationFeatureTemplate | Get Multicast Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations/{id}` | updateMulticastConfigurationFeatureTemplate | Update Multicast Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations/{id}` | deleteMulticastConfigurationFeatureTemplate | Delete Multicast Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/wirelessProfiles` | getWirelessProfiles | Get Wireless Profiles | Query: limit, offset, wirelessProfileName |
| POST | `/dna/intent/api/v1/wirelessProfiles` | createWirelessProfile | Create Wireless Profile |  |
| GET | `/dna/intent/api/v1/wirelessControllers/meshApNeighbours` | getMeshApNeighbours | Get Mesh Ap Neighbours | Query: wlcIpAddress, apName, ethernetMacAddress |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/anchorManagedApLocations` | getAnchorManagedAPLocationsForSpecificWirelessController | Get Anchor Managed AP Locations for specific Wireless Controller | networkDeviceId | Query: limit, offset |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralConfigurations/{id}` | updateRRMGeneralConfigurationFeatureTemplate | Update RRM General Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralConfigurations/{id}` | deleteRRMGeneralConfigurationFeatureTemplate | Delete RRM General Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralConfigurations/{id}` | getRRMGeneralConfigurationFeatureTemplate | Get RRM General Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/featureTemplates/wireless/dot11axConfigurations/{id}` | getDot11axConfigurationFeatureTemplate | Get Dot11ax Configuration Feature Template | id |
| PUT | `/dna/intent/api/v1/featureTemplates/wireless/dot11axConfigurations/{id}` | updateDot11axConfigurationFeatureTemplate | Update Dot11ax Configuration Feature Template | id |
| DELETE | `/dna/intent/api/v1/featureTemplates/wireless/dot11axConfigurations/{id}` | deleteDot11axConfigurationFeatureTemplate | Delete Dot11ax Configuration Feature Template | id |
| GET | `/dna/intent/api/v1/wirelessSettings/dot11beProfiles/count` | get802.11beProfilesCount | Get 802.11be Profiles Count |  |
| GET | `/dna/intent/api/v1/wirelessSettings/ssids/overrideAtSites` | retrieveSitesWithOverriddenSSIDs | Retrieve sites with overridden SSIDs | Query: siteId, offset, limit |
| GET | `/dna/intent/api/v1/wireless/accesspoint-configuration/summary` | getAccessPointConfiguration | Get Access Point Configuration | Query: key, wlcIpAddress, apMode, apModel, meshRole, provisioned, limit, offset |
| POST | `/dna/intent/api/v1/wirelessControllers/{deviceId}/provision` | wirelessControllerProvision | Wireless Controller Provision | deviceId |
| GET | `/dna/intent/api/v1/wirelessControllers/anchorCapableDevices` | getAnchorCapableDevices | Get Anchor capable devices |  |
| GET | `/dna/intent/api/v1/wirelessSettings/apProfiles/count` | getAPProfilesCount | Get AP Profiles Count |  |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/flexConnectConfigurations` | createFlexConnectConfigurationFeatureTemplate | Create Flex Connect Configuration Feature Template |  |
| POST | `/dna/intent/api/v1/wirelessControllers/{deviceId}/assignManagedApLocations` | assignManagedAPLocationsForWLC | Assign Managed AP Locations For WLC | deviceId |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/secondaryManagedApLocations` | getSecondaryManagedAPLocationsForSpecificWirelessController | Get Secondary Managed AP Locations for specific Wireless Controller | networkDeviceId | Query: limit, offset |
| POST | `/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequest/provision` | factoryResetAccessPoint(s) | Factory Reset Access Point(s) |  |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags` | retrieveAllSiteTagsForAWirelessProfile | Retrieve all Site Tags for a Wireless Profile | id | Query: limit, offset, siteTagName |
| GET | `/dna/intent/api/v1/device-reboot/apreboot/status` | getAccessPointRebootTaskResult | Get Access Point Reboot task result | Query: parentTaskId |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/apAuthorizationLists` | getAPAuthorizationListByNetworkDeviceId | Get AP Authorization List by network device Id | networkDeviceId |
| GET | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/count` | retrieveTheCountOfSiteTagsForAWirelessProfile | Retrieve the count of Site Tags for a Wireless Profile | id |
| POST | `/dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/mobilityReset` | mobilityReset | Mobility Reset |  |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralConfigurations` | createRRMGeneralConfigurationFeatureTemplate | Create RRM General Configuration Feature Template |  |
| GET | `/dna/intent/api/v1/wirelessControllers/{networkDeviceId}/managedApLocations/count` | getManagedAPLocationsCountForSpecificWirelessController | Get Managed AP Locations Count for specific Wireless Controller | networkDeviceId |
| POST | `/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfigurations` | createRRMFRAConfigurationFeatureTemplate | Create RRM FRA Configuration Feature Template |  |
| GET | `/dna/intent/api/v1/wirelessSettings/rfProfiles/count` | getRFProfilesCount | Get RF Profiles Count |  |
| GET | `/dna/intent/api/v1/wireless/accesspoint-configuration/details/{task_id}` | getAccessPointConfigurationTaskResult | Get Access Point Configuration task result | task_id |
| GET | `/intent/api/v1/wirelessSettings/interfaces/count` | getInterfacesCount | Get Interfaces Count |  |
| POST | `/dna/intent/api/v1/wireless/psk-override` | pSKOverride | PSK override |  |
| POST | `/dna/intent/api/v1/business/ssid` | createAndProvisionSSID | Create and Provision SSID |  |
| POST | `/dna/intent/api/v1/wireless/profile` | createWirelessProfile-2 | Create Wireless Profile |  |
| PUT | `/dna/intent/api/v1/wireless/profile` | updateWirelessProfile-2 | Update Wireless Profile |  |
| GET | `/dna/intent/api/v1/wireless/profile` | getWirelessProfile | Get Wireless Profile | Query: profileName |
| DELETE | `/dna/intent/api/v1/wireless/rf-profile/{rfProfileName}` | deleteRFProfiles | Delete RF profiles | rfProfileName |
| POST | `/dna/intent/api/v1/enterprise-ssid` | createEnterpriseSSID | Create Enterprise SSID |  |
| PUT | `/dna/intent/api/v1/enterprise-ssid` | updateEnterpriseSSID | Update Enterprise SSID |  |
| GET | `/dna/intent/api/v1/enterprise-ssid` | getEnterpriseSSID | Get Enterprise SSID | Query: ssidName |
| GET | `/dna/intent/api/v1/wireless/rf-profile` | retrieveRFProfiles | Retrieve RF profiles | Query: rf-profile-name |
| POST | `/dna/intent/api/v1/wireless/rf-profile` | createOrUpdateRFProfile | Create or Update RF profile |  |
| GET | `/dna/intent/api/v1/AssuranceGetSensorTestResults` | sensorTestResults | Sensor Test Results | Query: siteId, startTime, endTime, testFailureBy |
| POST | `/dna/intent/api/v1/wireless/provision` | provision | Provision |  |
| PUT | `/dna/intent/api/v1/wireless/provision` | provisionUpdate | Provision update |  |
| DELETE | `/dna/intent/api/v1/business/ssid/{ssidName}/{managedAPLocations}` | deleteSSIDAndProvisionItToDevices | Delete SSID and provision it to devices | ssidName, managedAPLocations |
| DELETE | `/dna/intent/api/v1/wireless-profile/{wirelessProfileName}` | deleteWirelessProfile-2 | Delete Wireless Profile | wirelessProfileName |
| POST | `/dna/intent/api/v1/wireless/ap-provision` | aPProvision-2 | AP Provision |  |
| DELETE | `/dna/intent/api/v1/wireless/dynamic-interface` | deleteDynamicInterface | Delete dynamic interface | Query: interfaceName |
| GET | `/dna/intent/api/v1/wireless/dynamic-interface` | getDynamicInterface | Get dynamic interface | Query: interface-name |
| POST | `/dna/intent/api/v1/wireless/dynamic-interface` | createUpdateDynamicInterface | Create Update Dynamic interface |  |
| DELETE | `/dna/intent/api/v1/enterprise-ssid/{ssidName}` | deleteEnterpriseSSID | Delete Enterprise SSID | ssidName |

### Ecosystem Integrations

#### ITSM

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/cmdb-sync/detail` | getCMDBSyncStatus | Get CMDB Sync Status | Query: status, date |
| GET | `/dna/intent/api/v1/integration/events` | getFailedITSMEvents | Get Failed ITSM Events | Query: instanceId |
| POST | `/dna/intent/api/v1/integration/events` | retryIntegrationEvents | Retry Integration Events |  |

### Event Management

#### 

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/event/syslog-config` | createSyslogDestination | Create Syslog Destination |  |
| GET | `/dna/intent/api/v1/event/syslog-config` | getSyslogDestination | Get Syslog Destination | Query: configId, name, protocol, offset, limit, sortBy, order |
| PUT | `/dna/intent/api/v1/event/syslog-config` | updateSyslogDestination | Update Syslog Destination |  |
| PUT | `/dna/intent/api/v1/event/webhook` | updateWebhookDestination | Update Webhook Destination |  |
| GET | `/dna/intent/api/v1/event/webhook` | getWebhookDestination | Get Webhook Destination | Query: webhookIds, offset, limit, sortBy, order |
| POST | `/dna/intent/api/v1/event/webhook` | createWebhookDestination | Create Webhook Destination |  |
| POST | `/dna/intent/api/v1/event/snmp-config` | createSNMPDestination | Create SNMP Destination |  |
| PUT | `/dna/intent/api/v1/event/snmp-config` | updateSNMPDestination | Update SNMP Destination |  |
| GET | `/dna/intent/api/v1/event/event-series/count` | countOfNotifications | Count of Notifications | Query: eventIds, startTime, endTime, category, type, severity, domain, subDomain, source |
| GET | `/dna/intent/api/v1/event/subscription-details/syslog` | getSyslogSubscriptionDetails | Get Syslog Subscription Details | Query: name, instanceId, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/event/subscription/count` | countOfEventSubscriptions | Count of Event Subscriptions | Query: eventIds |
| GET | `/dna/intent/api/v1/event/subscription-details/email` | getEmailSubscriptionDetails | Get Email Subscription Details | Query: name, instanceId, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/event/subscription/email` | getEmailEventSubscriptions | Get Email Event Subscriptions | Query: eventIds, offset, limit, sortBy, order, domain, subDomain, category, type, name |
| POST | `/dna/intent/api/v1/event/subscription/email` | createEmailEventSubscription | Create Email Event Subscription |  |
| PUT | `/dna/intent/api/v1/event/subscription/email` | updateEmailEventSubscription | Update Email Event Subscription |  |
| GET | `/dna/intent/api/v1/events` | getEvents | Get Events | Query: eventId, tags, offset, limit, sortBy, order |
| GET | `/dna/data/api/v1/event/event-series/audit-log/summary` | getAuditLogSummary | Get AuditLog Summary | Query: parentInstanceId, isParentOnly, instanceId, name, eventId, category, severity, domain, subDomain, source, userId, context, eventHierarchy, siteId, deviceId, isSystemEvents, description, startTime, endTime |
| POST | `/dna/intent/api/v1/event/subscription` | createEventSubscriptions | Create Event Subscriptions |  |
| PUT | `/dna/intent/api/v1/event/subscription` | updateEventSubscriptions | Update Event Subscriptions |  |
| DELETE | `/dna/intent/api/v1/event/subscription` | deleteEventSubscriptions | Delete Event Subscriptions | Query: subscriptions |
| GET | `/dna/intent/api/v1/event/subscription` | getEventSubscriptions | Get Event Subscriptions | Query: eventIds, offset, limit, sortBy, order |
| GET | `/dna/system/api/v1/event/artifact` | getEventArtifacts | Get EventArtifacts | Query: eventIds, tags, offset, limit, sortBy, order, search |
| PUT | `/dna/intent/api/v1/event/subscription/syslog` | updateSyslogEventSubscription | Update Syslog Event Subscription |  |
| POST | `/dna/intent/api/v1/event/subscription/syslog` | createSyslogEventSubscription | Create Syslog Event Subscription |  |
| GET | `/dna/intent/api/v1/event/subscription/syslog` | getSyslogEventSubscriptions | Get Syslog Event Subscriptions | Query: eventIds, offset, limit, sortBy, order, domain, subDomain, category, type, name |
| GET | `/dna/intent/api/v1/events/count` | countOfEvents | Count of Events | Query: eventId, tags |
| POST | `/dna/intent/api/v1/event/email-config` | createEmailDestination | Create Email Destination |  |
| PUT | `/dna/intent/api/v1/event/email-config` | updateEmailDestination | Update Email Destination |  |
| GET | `/dna/intent/api/v1/event/email-config` | getEmailDestination | Get Email Destination |  |
| GET | `/dna/data/api/v1/event/event-series/audit-logs` | getAuditLogRecords | Get AuditLog Records | Query: parentInstanceId, instanceId, name, eventId, category, severity, domain, subDomain, source, userId, context, eventHierarchy, siteId, deviceId, isSystemEvents, description, offset, limit, startTime, endTime, sortBy, order |
| GET | `/dna/intent/api/v1/event/event-series` | getNotifications | Get Notifications | Query: eventIds, startTime, endTime, category, type, severity, domain, subDomain, source, offset, limit, sortBy, order, tags, namespace, siteId |
| POST | `/dna/intent/api/v1/event/subscription/rest` | createRest/WebhookEventSubscription | Create Rest/Webhook Event Subscription |  |
| PUT | `/dna/intent/api/v1/event/subscription/rest` | updateRest/WebhookEventSubscription | Update Rest/Webhook Event Subscription |  |
| GET | `/dna/intent/api/v1/event/subscription/rest` | getRest/WebhookEventSubscriptions | Get Rest/Webhook Event Subscriptions | Query: eventIds, offset, limit, sortBy, order, domain, subDomain, category, type, name |
| GET | `/dna/data/api/v1/event/event-series/audit-log/parent-records` | getAuditLogParentRecords | Get AuditLog Parent Records | Query: instanceId, name, eventId, category, severity, domain, subDomain, source, userId, context, eventHierarchy, siteId, deviceId, isSystemEvents, description, offset, limit, startTime, endTime, sortBy, order |
| GET | `/dna/system/api/v1/event/artifact/count` | eventArtifactCount | EventArtifact Count |  |
| GET | `/dna/system/api/v1/event/config/connector-types` | getConnectorTypes | Get Connector Types |  |
| GET | `/dna/intent/api/v1/event/subscription-details/rest` | getRest/WebhookSubscriptionDetails | Get Rest/Webhook Subscription Details | Query: name, instanceId, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/dna-event/snmp-config` | getSNMPDestination | Get SNMP Destination | Query: configId, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/event/api-status/{executionId}` | getStatusAPIForEvents | Get Status API for Events | executionId |

### Integrations

#### ITSM Integration

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/integration-settings/instances/itsm` | createITSMIntegrationSetting | Create ITSM Integration setting |  |
| GET | `/dna/intent/api/v1/integration-settings/instances/itsm/{instanceId}` | getITSMIntegrationSettingById | Get ITSM Integration setting by Id | instanceId |
| PUT | `/dna/intent/api/v1/integration-settings/instances/itsm/{instanceId}` | updateITSMIntegrationSetting | Update ITSM Integration setting | instanceId |
| DELETE | `/dna/intent/api/v1/integration-settings/instances/itsm/{instanceId}` | deleteITSMIntegrationSetting | Delete ITSM Integration setting | instanceId |
| GET | `/dna/intent/api/v1/integration-settings/itsm/instances` | getAllITSMIntegrationSettings | Get all ITSM Integration settings | Query: page_size, page, sortBy, order |
| GET | `/dna/intent/api/v1/integration-settings/status` | getITSMIntegrationStatus | Get ITSM Integration status |  |

### Know Your Network

#### 

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/data/api/v1/energy/trendAnalytics` | getEnergyTrendAnalytics | Get energy trend analytics |  |
| POST | `/dna/data/api/v1/energy/summaryAnalytics` | getEnergySummaryAnalytics | Get energy summary analytics |  |

#### Applications

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/data/api/v1/networkApplications` | retrievesTheListOfNetworkApplicationsAlongWithExperienceAndHealthMetrics | Retrieves the list of network applications along with experience and health metrics | Query: startTime, endTime, limit, offset, sortBy, order, siteId, ssid, applicationName, businessRelevance, attribute |
| GET | `/dna/data/api/v1/thousandEyesTestResults/trendAnalytics` | theTrendAnalyticsDataForThousandEyesTestResultsInTheSpecifiedTimeRange | The trend analytics data for ThousandEyes test results in the specified time range | Query: siteId, startTime, endTime, trendInterval, testId, testName, testType, agentId, networkDeviceName, limit, offset, order |
| POST | `/dna/data/api/v1/networkApplications/trendAnalytics` | retrievesTheTrendAnalyticsDataRelatedToNetworkApplications. | Retrieves the Trend analytics data related to network applications. |  |
| GET | `/dna/data/api/v1/thousandEyesTestResults` | retrievesTheListOfThousandEyesTestResultsAlongWithRelatedMetrics | Retrieves the list of ThousandEyes test results along with related metrics | Query: siteId, startTime, endTime, testId, testName, testType, agentId, networkDeviceName, attribute, limit, offset, sortBy, order |
| GET | `/dna/data/api/v1/thousandEyesTestResults/count` | retrievesTheTotalCountOfThousandEyesTestResults | Retrieves the total count of ThousandEyes test results | Query: siteId, startTime, endTime, testId, testName, testType, agentId, networkDeviceName |
| POST | `/dna/data/api/v1/networkApplications/{id}/trendAnalytics` | retrievesTheTrendAnalyticsRelatedToSpecificNetworkApplication. | Retrieves the Trend analytics related to specific network application. | id |
| GET | `/dna/data/api/v1/networkApplications/count` | retrievesTheTotalCountOfNetworkApplicationsByApplyingBasicFiltering | Retrieves the total count of network applications by applying basic filtering | Query: startTime, endTime, siteId, ssid, applicationName, businessRelevance |
| POST | `/dna/data/api/v1/networkApplications/summaryAnalytics` | retrievesSummaryAnalyticsDataRelatedToNetworkApplicationsAlongWithHealthMetrics. | Retrieves summary analytics data related to network applications along with health metrics. |  |
| GET | `/dna/intent/api/v1/application-health` | applications | Applications | Query: siteId, deviceId, macAddress, startTime, endTime, applicationHealth, offset, limit, applicationName |

#### Clients

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/client-detail` | getClientDetail | Get Client Detail | Query: macAddress, timestamp |
| POST | `/dna/data/api/v1/energy/clients/query` | queryClientsEnergy | Query clients energy |  |
| GET | `/dna/intent/api/v1/client-health` | getOverallClientHealth | Get Overall Client Health | Query: timestamp |
| POST | `/dna/data/api/v1/energy/clients/query/count` | countClientsEnergyFromQuery | Count clients energy from query |  |
| POST | `/dna/data/api/v1/clients/trendAnalytics` | retrievesTheTrendAnalyticsDataRelatedToClients. | Retrieves the Trend analytics data related to clients. |  |
| GET | `/dna/data/api/v1/clients/{id}` | retrievesSpecificClientInformationMatchingTheMACAddress. | Retrieves specific client information matching the MAC address. | id | Query: startTime, endTime, view, attribute |
| GET | `/dna/data/api/v1/energy/clients` | getClientsEnergy | Get clients energy | Query: startTime, endTime, limit, cursor, sortBy, order, id, siteId, siteHierarchy, siteHierarchyId, deviceCategory, deviceSubCategory, view, attribute |
| GET | `/dna/data/api/v1/clients/count` | retrievesTheTotalCountOfClientsByApplyingBasicFiltering | Retrieves the total count of clients by applying basic filtering | Query: startTime, endTime, type, osType, osVersion, siteHierarchy, siteHierarchyId, siteId, ipv4Address, ipv6Address, macAddress, wlcName, connectedNetworkDeviceName, ssid, band |
| GET | `/dna/data/api/v1/energy/clients/count` | countClientsEnergy | Count clients energy | Query: startTime, endTime, id, siteId, siteHierarchy, siteHierarchyId, deviceCategory, deviceSubCategory |
| GET | `/dna/data/api/v1/energy/clients/{id}` | getClientEnergyByID | Get client energy by ID | id | Query: startTime, endTime, view, attribute |
| POST | `/dna/data/api/v1/clients/query/count` | retrievesTheNumberOfClientsByApplyingComplexFilters. | Retrieves the number of clients by applying complex filters. |  |
| POST | `/dna/data/api/v1/clients/{id}/trendAnalytics` | retrievesSpecificClientInformationOverASpecifiedPeriodOfTime. | Retrieves specific client information over a specified period of time. | id |
| POST | `/dna/data/api/v1/clients/summaryAnalytics` | retrievesSummaryAnalyticsDataRelatedToClients. | Retrieves summary analytics data related to clients. |  |
| POST | `/dna/data/api/v1/clients/topNAnalytics` | retrievesTheTop-NAnalyticsDataRelatedToClients. | Retrieves the Top-N analytics data related to clients. |  |
| POST | `/dna/data/api/v1/clients/query` | retrievesTheListOfClientsByApplyingComplexFiltersWhileAlsoSupportingAggregateAttributes. | Retrieves the list of clients by applying complex filters while also supporting aggregate attributes. |  |
| GET | `/dna/data/api/v1/clients` | retrievesTheListOfClients,WhileAlsoOfferingBasicFilteringAndSortingCapabilities. | Retrieves the list of clients, while also offering basic filtering and sorting capabilities. | Query: startTime, endTime, limit, offset, sortBy, order, type, osType, osVersion, siteHierarchy, siteHierarchyId, siteId, ipv4Address, ipv6Address, macAddress, wlcName, connectedNetworkDeviceName, ssid, band, view, attribute |
| GET | `/dna/intent/api/v1/client-proximity` | clientProximity | Client Proximity | Query: username, number_days, time_resolution |
| GET | `/dna/intent/api/v1/client-enrichment-details` | getClientEnrichmentDetails | Get Client Enrichment Details |  |

#### Compliance

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/securityAdvisories/trials` | createsATrialForSecurityAdvisoriesDetectionOnNetworkDevices | Creates a trial for security advisories detection on network devices |  |
| GET | `/dna/intent/api/v1/securityAdvisories/trials` | getTrialDetailsForSecurityAdvisoriesDetectionOnNetworkDevices | Get trial details for security advisories detection on network devices |  |
| GET | `/dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}/bugs` | getBugsAffectingTheNetworkDevice | Get bugs affecting the network device | networkDeviceId | Query: id, severity, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/networkBugs/trials` | getTrialDetailsForBugsDetectionOnNetworkDevices | Get trial details for bugs detection on network devices |  |
| POST | `/dna/intent/api/v1/networkBugs/trials` | createsATrialForBugsDetectionOnNetworkDevices | Creates a trial for bugs detection on network devices |  |
| GET | `/dna/intent/api/v1/securityAdvisories/results/advisories/count` | getCountOfSecurityAdvisoriesAffectingTheNetworkDevices | Get count of security advisories affecting the network devices | Query: id, deviceCount, cvssBaseScore, securityImpactRating |
| GET | `/dna/intent/api/v1/fieldNotices/results/networkDevices/count` | getCountOfFieldNoticeNetworkDevices | Get count of field notice network devices | Query: networkDeviceId, scanStatus, noticeCount |
| GET | `/dna/intent/api/v1/networkBugs/results/bugs/{id}/networkDevices/count` | getCountOfNetworkBugDevicesForTheBug | Get count of network bug devices for the bug | id | Query: networkDeviceId, scanMode, scanStatus |
| GET | `/dna/intent/api/v1/securityAdvisories/results/advisories/{id}/networkDevices/{networkDeviceId}` | getSecurityAdvisoryNetworkDeviceForTheSecurityAdvisoryByNetworkDeviceId | Get security advisory network device for the security advisory by network device id | id, networkDeviceId |
| GET | `/dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories` | getSecurityAdvisoriesAffectingTheNetworkDevice | Get security advisories affecting the network device | networkDeviceId | Query: id, cvssBaseScore, securityImpactRating, offset, limit, sortBy, order |
| POST | `/dna/intent/api/v1/fieldNotices/trials` | createsATrialForFieldNoticesDetectionOnNetworkDevices | Creates a trial for field notices detection on network devices |  |
| GET | `/dna/intent/api/v1/fieldNotices/trials` | getTrialDetailsForFieldNoticesDetectionOnNetworkDevices | Get trial details for field notices detection on network devices |  |
| GET | `/dna/intent/api/v1/networkBugs/results/bugs` | getNetworkBugs | Get network bugs | Query: id, deviceCount, severity, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/compliance/detail/count` | getComplianceDetailCount | Get Compliance Detail Count | Query: complianceType, complianceStatus |
| GET | `/dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}` | getNetworkBugDeviceByDeviceId | Get network bug device by device id | networkDeviceId |
| GET | `/dna/intent/api/v1/networkBugs/results/bugs/count` | getCountOfNetworkBugs | Get count of network bugs | Query: id, deviceCount, severity |
| GET | `/dna/intent/api/v1/securityAdvisories/results/advisories/{id}` | getSecurityAdvisoryAffectingTheNetworkDevicesById | Get security advisory affecting the network devices by Id | id |
| GET | `/dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices/count` | getCountOfFieldNoticeNetworkDevicesForTheNotice | Get count of field notice network devices for the notice | id | Query: networkDeviceId, scanStatus |
| GET | `/dna/intent/api/v1/compliance/{deviceUuid}/detail` | complianceDetailsOfDevice | Compliance Details of Device | deviceUuid | Query: category, complianceType, diffList, status, remediationSupported |
| POST | `/dna/intent/api/v1/network-device-config/write-memory` | commitDeviceConfiguration | Commit device configuration |  |
| GET | `/dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}/notices/count` | getCountOfFieldNoticesAffectingTheNetworkDevice | Get count of field notices affecting the network device | networkDeviceId | Query: id, type |
| POST | `/dna/intent/api/v1/networkBugs/triggerScan` | triggersABugsScanForTheSupportedNetworkDevices | Triggers a bugs scan for the supported network devices | Query: failedDevicesOnly |
| GET | `/dna/intent/api/v1/networkBugs/resultsTrend/count` | getCountOfNetworkBugsResultsTrendOverTime | Get count of network bugs results trend over time | Query: scanTime |
| GET | `/dna/intent/api/v1/networkBugs/resultsTrend` | getNetworkBugsResultsTrendOverTime | Get network bugs results trend over time | Query: scanTime, offset, limit |
| GET | `/dna/intent/api/v1/fieldNotices/resultsTrend` | getFieldNoticesResultsTrendOverTime | Get field notices results trend over time | Query: scanTime, offset, limit |
| GET | `/dna/intent/api/v1/fieldNotices/results/notices` | getFieldNotices | Get field notices | Query: id, deviceCount, type, offset, limit, sortBy, order |
| POST | `/dna/intent/api/v1/compliance/networkDevices/{id}/issues/remediation/provision` | complianceRemediation | Compliance Remediation | id |
| GET | `/dna/intent/api/v1/network-device-config/task` | getConfigTaskDetails | Get config task details | Query: parentTaskId |
| GET | `/dna/intent/api/v1/networkBugs/results/bugs/{id}/networkDevices/{networkDeviceId}` | getNetworkBugDeviceForTheBugByNetworkDeviceId | Get network bug device for the bug by network device id | id, networkDeviceId |
| GET | `/dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}/bugs/count` | getCountOfBugsAffectingTheNetworkDevice | Get count of bugs affecting the network device | networkDeviceId | Query: id, severity |
| GET | `/dna/intent/api/v1/compliance/{deviceUuid}` | deviceComplianceStatus | Device Compliance Status | deviceUuid |
| GET | `/dna/intent/api/v1/fieldNotices/results/notices/{id}` | getFieldNoticeById | Get field notice by Id | id |
| GET | `/dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}/notices/{id}` | getFieldNoticeAffectingTheNetworkDeviceByDeviceIdAndNoticeId | Get field notice affecting the network device by device Id and notice id | networkDeviceId, id |
| GET | `/dna/intent/api/v1/securityAdvisories/results/networkDevices/count` | getCountOfSecurityAdvisoryNetworkDevices | Get count of security advisory network devices | Query: networkDeviceId, scanMode, scanStatus, advisoryCount |
| POST | `/dna/intent/api/v1/securityAdvisories/triggerScan` | triggersASecurityAdvisoriesScanForTheSupportedNetworkDevices | Triggers a security advisories scan for the supported network devices | Query: failedDevicesOnly |
| GET | `/dna/intent/api/v1/securityAdvisories/results/advisories/{id}/networkDevices/count` | getCountOfSecurityAdvisoryNetworkDevicesForTheSecurityAdvisory | Get count of security advisory network devices for the security advisory | id | Query: networkDeviceId, scanMode, scanStatus |
| GET | `/dna/intent/api/v1/networkBugs/results/bugs/{id}/networkDevices` | getNetworkBugDevicesForTheBug | Get network bug devices for the bug | id | Query: networkDeviceId, scanMode, scanStatus, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}` | getSecurityAdvisoryNetworkDeviceByNetworkDeviceId | Get security advisory network device by network device id | networkDeviceId |
| GET | `/dna/intent/api/v1/securityAdvisories/resultsTrend/count` | getCountOfSecurityAdvisoriesResultsTrendOverTime | Get count of security advisories results trend over time | Query: scanTime |
| GET | `/dna/intent/api/v1/securityAdvisories/resultsTrend` | getSecurityAdvisoriesResultsTrendOverTime | Get security advisories results trend over time | Query: scanTime, offset, limit |
| GET | `/dna/intent/api/v1/securityAdvisories/results/networkDevices` | getSecurityAdvisoryNetworkDevices | Get security advisory network devices | Query: networkDeviceId, scanMode, scanStatus, advisoryCount, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/fieldNotices/results/notices/count` | getCountOfFieldNotices | Get count of field notices | Query: id, deviceCount, type |
| GET | `/dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories/{id}` | getSecurityAdvisoryAffectingTheNetworkDeviceByDeviceIdAndAdvisoryId | Get security advisory affecting the network device by device Id and advisory id | networkDeviceId, id |
| POST | `/dna/intent/api/v1/fieldNotices/triggerScan` | triggersAFieldNoticesScanForTheSupportedNetworkDevices | Triggers a field notices scan for the supported network devices | Query: failedDevicesOnly |
| GET | `/dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices` | getFieldNoticeNetworkDevicesForTheNotice | Get field notice network devices for the notice | id | Query: networkDeviceId, scanStatus, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/compliance` | getComplianceStatus | Get Compliance Status  | Query: complianceStatus, deviceUuid, offset, limit |
| GET | `/dna/intent/api/v1/fieldNotices/resultsTrend/count` | getCountOfFieldNoticesResultsTrendOverTime | Get count of field notices results trend over time | Query: scanTime |
| GET | `/dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices/{networkDeviceId}` | getFieldNoticeNetworkDeviceForTheNoticeByNetworkDeviceId | Get field notice network device for the notice by network device id | id, networkDeviceId |
| GET | `/dna/intent/api/v1/networkBugs/results/networkDevices/count` | getCountOfNetworkBugDevices | Get count of network bug devices | Query: networkDeviceId, scanMode, scanStatus, bugCount |
| GET | `/dna/intent/api/v1/compliance/count` | getComplianceStatusCount | Get Compliance Status Count | Query: complianceStatus |
| GET | `/dna/intent/api/v1/fieldNotices/results/networkDevices` | getFieldNoticeNetworkDevices | Get field notice network devices | Query: networkDeviceId, scanStatus, noticeCount, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories/count` | getCountOfSecurityAdvisoriesAffectingTheNetworkDevice | Get count of security advisories affecting the network device | networkDeviceId | Query: id, cvssBaseScore, securityImpactRating |
| GET | `/dna/intent/api/v1/compliance/detail` | getComplianceDetail | Get Compliance Detail  | Query: complianceType, complianceStatus, deviceUuid, offset, limit |
| GET | `/dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}/bugs/{id}` | getBugAffectingTheNetworkDeviceByDeviceIdAndBugId | Get bug affecting the network device by device Id and bug id | networkDeviceId, id |
| GET | `/dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}` | getFieldNoticeNetworkDeviceByDeviceId | Get field notice network device by device id | networkDeviceId |
| GET | `/dna/intent/api/v1/securityAdvisories/results/advisories` | getSecurityAdvisoriesAffectingTheNetworkDevices | Get security advisories affecting the network devices | Query: id, deviceCount, cvssBaseScore, securityImpactRating, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}/notices` | getFieldNoticesAffectingTheNetworkDevice | Get field notices affecting the network device | networkDeviceId | Query: id, type, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/securityAdvisories/results/advisories/{id}/networkDevices` | getSecurityAdvisoryNetworkDevicesForTheSecurityAdvisory | Get security advisory network devices for the security advisory | id | Query: networkDeviceId, scanMode, scanStatus, offset, limit, sortBy, order |
| POST | `/dna/intent/api/v1/compliance/` | runCompliance | Run Compliance |  |
| GET | `/dna/intent/api/v1/networkBugs/results/bugs/{id}` | getNetworkBugById | Get network bug by Id | id |
| GET | `/dna/intent/api/v1/networkBugs/results/networkDevices` | getNetworkBugDevices | Get network bug devices | Query: networkDeviceId, scanMode, scanStatus, bugCount, offset, limit, sortBy, order |

#### Devices

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/security/rogue/additional/details/count` | rogueAdditionalDetailCount | Rogue Additional Detail Count |  |
| GET | `/dna/intent/api/v1/security/threats/rogue/allowed-list` | getAllowedMacAddress | Get Allowed Mac Address | Query: offset, limit |
| POST | `/dna/intent/api/v1/security/threats/rogue/allowed-list` | addAllowedMacAddress | Add Allowed Mac Address |  |
| GET | `/dna/intent/api/v1/security/rogue/wireless-containment/status/{macAddress}` | wirelessRogueAPContainmentStatus | Wireless Rogue AP Containment Status | macAddress |
| POST | `/dna/intent/api/v1/security/rogue/additional/details` | rogueAdditionalDetails | Rogue Additional Details |  |
| POST | `/dna/intent/api/v1/security/threats/details/count` | threatDetailCount | Threat Detail Count |  |
| DELETE | `/dna/intent/api/v1/security/threats/rogue/allowed-list/{macAddress}` | removeAllowedMacAddress | Remove Allowed Mac Address | macAddress |
| POST | `/dna/intent/api/v1/security/threats/summary` | threatSummary | Threat Summary |  |
| POST | `/dna/data/api/v1/aaaServices/trendAnalytics` | getTrendAnalyticsDataOfAAAServicesForGivenSetOfComplexFilters. | Get trend analytics data of AAA Services for given set of complex filters. |  |
| POST | `/dna/intent/api/v1/security/rogue/wireless-containment/start` | startWirelessRogueAPContainment | Start Wireless Rogue AP Containment |  |
| GET | `/dna/intent/api/v1/security/threats/rogue/allowed-list/count` | getAllowedMacAddressCount | Get Allowed Mac Address Count |  |
| GET | `/dna/intent/api/v1/security/threats/level` | getThreatLevels | Get Threat Levels |  |
| GET | `/dna/intent/api/v1/network-device/{deviceId}/chassis` | getChassisDetailsForDevice | Get Chassis Details for Device | deviceId |
| GET | `/dna/intent/api/v1/security/threats/type` | getThreatTypes | Get Threat Types |  |
| POST | `/dna/intent/api/v1/security/rogue/wireless-containment/stop` | stopWirelessRogueAPContainment | Stop Wireless Rogue AP Containment |  |
| POST | `/dna/intent/api/v1/security/threats/details` | threatDetails | Threat Details |  |
| POST | `/dna/data/api/v1/networkDevices/{id}/trendAnalytics` | theTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRange | The Trend analytics data for the network Device in the specified time range | id |
| POST | `/dna/data/api/v1/networkDevices/trendAnalytics` | getsTheTrendAnalyticsData. | Gets the Trend analytics data. |  |
| GET | `/dna/intent/api/v1/network-device/user-defined-field` | getAllUser-Defined-Fields | Get All User-Defined-Fields | Query: id, name |
| POST | `/dna/intent/api/v1/network-device/user-defined-field` | createUser-Defined-Field | Create User-Defined-Field |  |
| GET | `/dna/intent/api/v1/network-device/module/{id}` | getModuleInfoById | Get Module Info by Id | id |
| GET | `/dna/data/api/v1/dnsServices` | retrievesTheListOfDNSServicesForGivenParameters. | Retrieves the list of DNS Services for given parameters. | Query: startTime, endTime, limit, offset, sortBy, order, serverIp, deviceId, deviceSiteHierarchyId, deviceSiteId, ssid |
| POST | `/dna/intent/api/v1/networkDevices/query` | queryNetworkDevicesWithFilters | Query network devices with filters |  |
| GET | `/dna/data/api/v1/assuranceEvents/{id}` | getDetailsOfASingleAssuranceEvent | Get details of a single assurance event | id | Query: attribute, view |
| DELETE | `/dna/intent/api/v1/network-device/{id}` | deleteDeviceById | Delete Device by Id | id | Query: cleanConfig |
| GET | `/dna/intent/api/v1/network-device/{id}` | getDeviceByID | Get Device by ID | id |
| POST | `/dna/intent/api/v1/healthScoreDefinitions/bulkUpdate` | updateHealthScoreDefinitions. | Update health score definitions. |  |
| POST | `/dna/intent/api/v1/networkDeviceMaintenanceSchedules` | createMaintenanceScheduleForNetworkDevices | Create maintenance schedule for network devices |  |
| GET | `/dna/intent/api/v1/networkDeviceMaintenanceSchedules` | retrieveScheduledMaintenanceWindowsForNetworkDevices | Retrieve scheduled maintenance windows for network devices | Query: networkDeviceIds, status, limit, offset, sortBy, order |
| POST | `/dna/data/api/v1/aaaServices/summaryAnalytics` | getSummaryAnalyticsDataOfAAAServicesForGivenSetOfComplexFilters. | Get summary analytics data of AAA Services for given set of complex filters. |  |
| GET | `/dna/intent/api/v1/network-device/{deviceUuid}/equipment` | getTheDetailsOfPhysicalComponentsOfTheGivenDevice. | Get the Details of Physical Components of the Given Device. | deviceUuid | Query: type |
| GET | `/dna/data/api/v1/assuranceEvents` | queryAssuranceEvents | Query assurance events | Query: deviceFamily, startTime, endTime, messageType, severity, siteId, siteHierarchyId, networkDeviceName, networkDeviceId, apMac, clientMac, attribute, view, offset, limit, sortBy, order |
| POST | `/dna/data/api/v1/networkDevices/summaryAnalytics` | getsTheSummaryAnalyticsDataRelatedToNetworkDevices. | Gets the summary analytics data related to network devices. |  |
| GET | `/dna/intent/api/v1/network-device` | getDeviceList | Get Device list | Query: hostname, managementIpAddress, macAddress, locationName, serialNumber, location, family, type, series, collectionStatus, collectionInterval, notSyncedForMinutes, errorCode, errorDescription, softwareVersion, softwareType, platformId, role, reachabilityStatus, upTime, associatedWlcIp, license.name, license.type, license.status, module+name, module+equpimenttype, module+servicestate, module+vendorequipmenttype, module+partnumber, module+operationstatecode, id, deviceSupportLevel, offset, limit |
| POST | `/dna/intent/api/v1/network-device` | addDevice | Add Device |  |
| PUT | `/dna/intent/api/v1/network-device` | updateDeviceDetails | Update Device Details |  |
| GET | `/dna/intent/api/v1/network-device/{deviceUuid}/interface/poe-detail` | returnsPOEInterfaceDetailsForTheDevice. | Returns POE interface details for the device. | deviceUuid | Query: interfaceNameList |
| PUT | `/dna/intent/api/v1/networkDevices/resyncIntervalSettings` | updateGlobalResyncInterval | Update global resync interval |  |
| POST | `/dna/intent/api/v1/interface/{interfaceUuid}/operation` | clearMac-AddressTable | Clear Mac-Address table | interfaceUuid | Query: deploymentMode |
| POST | `/dna/data/api/v1/networkDevices/query/count` | getsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions. | Gets the total number Network Devices based on the provided complex filters and aggregation functions. |  |
| GET | `/dna/intent/api/v1/network-device/{id}/vlan` | getDeviceInterfaceVLANs | Get Device Interface VLANs | id | Query: interfaceType |
| GET | `/dna/intent/api/v1/networkDevices/{id}` | getDetailsOfASingleNetworkDevice | Get details of a single network device | id | Query: views |
| GET | `/dna/data/api/v1/assuranceEvents/count` | countTheNumberOfEvents | Count the number of events | Query: deviceFamily, startTime, endTime, messageType, severity, siteId, siteHierarchyId, networkDeviceName, networkDeviceId, apMac, clientMac |
| GET | `/dna/data/api/v1/dhcpServices/{id}` | retrievesTheDetailsOfASpecificDHCPServiceMatchingTheIdOfTheService. | Retrieves the details of a specific DHCP Service matching the id of the Service. | id | Query: startTime, endTime |
| PUT | `/dna/intent/api/v1/floors/{floorId}/planned-access-points` | updatePlannedAccessPointForFloor | Update Planned Access Point for Floor | floorId |
| GET | `/dna/intent/api/v1/floors/{floorId}/planned-access-points` | getPlannedAccessPointsForFloor | Get Planned Access Points for Floor | floorId | Query: limit, offset, radios |
| POST | `/dna/intent/api/v1/floors/{floorId}/planned-access-points` | createPlannedAccessPointForFloor | Create Planned Access Point for Floor | floorId |
| GET | `/dna/data/api/v1/aaaServices/{id}` | retrievesTheDetailsOfASpecificAAAServiceMatchingTheIdOfTheService. | Retrieves the details of a specific AAA Service matching the id of the Service. | id | Query: startTime, endTime |
| GET | `/dna/intent/api/v1/device-health` | devices | Devices | Query: deviceRole, siteId, health, startTime, endTime, limit, offset |
| GET | `/dna/intent/api/v1/network-device/collection-schedule/global` | getPollingIntervalForAllDevices | Get Polling Interval for all devices |  |
| PUT | `/dna/intent/api/v1/network-device/sync` | syncDevices | Sync Devices | Query: forceSync |
| GET | `/dna/intent/api/v1/interface/network-device/{deviceId}/{startIndex}/{recordsToReturn}` | getDeviceInterfacesBySpecifiedRange | Get Device Interfaces by specified range | deviceId, startIndex, recordsToReturn |
| GET | `/dna/data/api/v1/interfaces/count` | getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange.WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount. | Gets the total Network device interface counts in the specified time range. When there is no start and end time specified returns the latest interfaces total count. | Query: startTime, endTime, siteHierarchy, siteHierarchyId, siteId, networkDeviceId, networkDeviceIpAddress, networkDeviceMacAddress, interfaceId, interfaceName |
| POST | `/dna/intent/api/v1/networkDevices/resyncIntervalSettings/override` | overrideResyncInterval | Override resync interval |  |
| GET | `/dna/data/api/v1/dnsServices/count` | retrievesTheTotalNumberOfDNSServicesForGivenParameters. | Retrieves the total number of DNS Services for given parameters. | Query: startTime, endTime, serverIp, deviceId, deviceSiteHierarchyId, deviceSiteId, ssid |
| GET | `/dna/intent/api/v1/interface/count` | getDeviceInterfaceCountForMultipleDevices | Get Device Interface Count for Multiple Devices |  |
| POST | `/dna/data/api/v1/interfaces/query` | getsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions | Gets the list of interfaces across the Network Devices based on the provided complex filters and aggregation functions |  |
| GET | `/dna/intent/api/v1/network-device/{deviceUuid}/line-card` | getLinecardDetails | Get Linecard details | deviceUuid |
| GET | `/dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings` | getResyncIntervalForTheNetworkDevice | Get resync interval for the network device | id |
| PUT | `/dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings` | updateResyncIntervalForTheNetworkDevice | Update resync interval for the network device | id |
| GET | `/dna/intent/api/v1/interface/network-device/{deviceId}/interface-name` | getInterfaceDetailsByDeviceIdAndInterfaceName | Get Interface details by device Id and interface name | deviceId | Query: name |
| POST | `/dna/data/api/v1/dhcpServices/query/count` | retrievesTheTotalNumberOfDHCPServicesForGivenSetOfComplexFilters. | Retrieves the total number of DHCP Services for given set of complex filters. |  |
| POST | `/dna/intent/api/v1/networkDevices/deleteWithCleanup` | deleteNetworkDeviceWithConfigurationCleanup | Delete network device with configuration cleanup |  |
| GET | `/dna/data/api/v1/energy/networkDevices/count` | countDevicesEnergy | Count devices energy | Query: startTime, endTime, id, siteId, siteHierarchy, siteHierarchyId, deviceCategory, deviceSubCategory |
| GET | `/dna/intent/api/v1/healthScoreDefinitions/count` | getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters. | Get the count of health score definitions based on provided filters. | Query: deviceType, id, includeForOverallHealth |
| POST | `/dna/data/api/v1/networkDevices/topNAnalytics` | getsTheTop-NAnalyticsDataRelatedToNetworkDevices. | Gets the Top-N analytics data related to network devices. |  |
| GET | `/dna/intent/api/v1/network-device/insight/{siteId}/device-link` | inventoryInsightDeviceLinkMismatchAPI | Inventory Insight Device Link Mismatch API | siteId | Query: offset, limit, category, sortBy, order |
| GET | `/dna/intent/api/v1/network-device/count` | getDeviceCount | Get Device Count | Query: hostname, managementIpAddress, macAddress, locationName |
| POST | `/dna/data/api/v1/aaaServices/query` | retrievesTheListOfAAAServicesForGivenSetOfComplexFilters. | Retrieves the list of AAA Services for given set of complex filters. |  |
| GET | `/dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id}` | retrievesTheMaintenanceScheduleInformation. | Retrieves the maintenance schedule information. | id |
| PUT | `/dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id}` | updatesTheMaintenanceScheduleInformation | Updates the maintenance schedule information | id |
| DELETE | `/dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id}` | deleteMaintenanceSchedule. | Delete maintenance schedule. | id |
| GET | `/dna/intent/api/v1/interface/network-device/{deviceId}/count` | getDeviceInterfaceCount | Get Device Interface count | deviceId |
| POST | `/dna/data/api/v1/dnsServices/{id}/trendAnalytics` | getTrendAnalyticsDataForAGivenDNSServiceMatchingTheIdOfTheService. | Get trend analytics data for a given DNS Service matching the id of the Service. | id |
| GET | `/dna/data/api/v1/networkDevices/{id}` | getTheDeviceDataForTheGivenDeviceId(Uuid) | Get the device data for the given device id (Uuid) | id | Query: startTime, endTime, view, attribute |
| GET | `/dna/intent/api/v1/networkDeviceMaintenanceSchedules/count` | retrieveTheTotalNumberOfScheduledMaintenanceWindows | Retrieve the total number of scheduled maintenance windows | Query: networkDeviceIds, status |
| GET | `/dna/intent/api/v1/interface/ospf` | getOSPFInterfaces | Get OSPF interfaces |  |
| GET | `/dna/data/api/v1/energy/networkDevices` | getDevicesEnergy | Get devices energy | Query: startTime, endTime, limit, cursor, sortBy, order, id, siteId, siteHierarchy, siteHierarchyId, deviceCategory, deviceSubCategory, view, attribute |
| POST | `/dna/data/api/v1/dnsServices/summaryAnalytics` | getSummaryAnalyticsDataOfDNSServicesForGivenSetOfComplexFilters. | Get summary analytics data of DNS Services for given set of complex filters. |  |
| POST | `/dna/data/api/v1/dhcpServices/trendAnalytics` | getTrendAnalyticsDataOfDHCPServicesForGivenSetOfComplexFilters. | Get trend analytics data of DHCP Services for given set of complex filters. |  |
| POST | `/dna/intent/api/v2/networkDevices/{deviceId}/interfaces/query` | getDeviceInterfaceStatsInfo | Get Device Interface Stats Info | deviceId |
| DELETE | `/dna/intent/api/v1/network-device/user-defined-field/{id}` | deleteUser-Defined-Field | Delete User-Defined-Field | id |
| PUT | `/dna/intent/api/v1/network-device/user-defined-field/{id}` | updateUser-Defined-Field | Update User-Defined-Field | id |
| GET | `/dna/intent/api/v1/network-device/{deviceId}/stack` | getStackDetailsForDevice | Get Stack Details for Device | deviceId |
| POST | `/dna/data/api/v1/aaaServices/topNAnalytics` | getTopNAnalyticsDataOfAAAServicesForGivenSetOfComplexFilters. | Get Top N analytics data of AAA Services for given set of complex filters. |  |
| DELETE | `/dna/intent/api/v1/floors/{floorId}/planned-access-points/{plannedAccessPointUuid}` | deletePlannedAccessPointForFloor | Delete Planned Access Point for Floor | floorId, plannedAccessPointUuid |
| GET | `/dna/intent/api/v1/network-device/functional-capability/{id}` | getFunctionalCapabilityById | Get Functional Capability by Id | id |
| POST | `/dna/data/api/v1/energy/networkDevices/query` | queryDevicesEnergy. | Query devices energy. |  |
| POST | `/dna/intent/api/v1/networkDevices/query/count` | countTheNumberOfNetworkDevicesWithFilters | Count the number of network devices with filters |  |
| GET | `/dna/intent/api/v1/interface/isis` | getISISInterfaces | Get ISIS interfaces |  |
| POST | `/dna/data/api/v1/dhcpServices/summaryAnalytics` | getSummaryAnalyticsDataOfDHCPServicesForGivenSetOfComplexFilters. | Get summary analytics data of DHCP Services for given set of complex filters. |  |
| GET | `/dna/intent/api/v1/network-device/config/count` | getDeviceConfigCount | Get Device Config Count |  |
| GET | `/dna/intent/api/v1/network-device/{deviceUuid}/poe` | pOEDetails | POE details  | deviceUuid |
| GET | `/dna/intent/api/v1/network-device/{id}/brief` | getDeviceSummary | Get Device Summary | id |
| GET | `/dna/intent/api/v1/network-device/module/count` | getModuleCount | Get Module count | Query: deviceId, nameList, vendorEquipmentTypeList, partNumberList, operationalStateCodeList |
| GET | `/dna/intent/api/v1/network-device/{networkDeviceId}/config` | getDeviceConfigById | Get Device Config by Id | networkDeviceId |
| GET | `/dna/intent/api/v1/network-device/{id}/collection-schedule` | getPollingIntervalById | Get Polling Interval by Id | id |
| PUT | `/dna/intent/api/v1/interface/{interfaceUuid}` | updateInterfaceDetails | Update Interface details | interfaceUuid | Query: deploymentMode |
| GET | `/dna/data/api/v1/dhcpServices/count` | retrievesTheTotalNumberOfDHCPServicesForGivenParameters. | Retrieves the total number of DHCP Services for given parameters. | Query: startTime, endTime, serverIp, deviceId, deviceName, deviceSiteHierarchy, deviceSiteHierarchyId, deviceSiteId |
| GET | `/dna/data/api/v1/dnsServices/{id}` | retrievesTheDetailsOfASpecificDNSServiceMatchingTheIdOfTheService. | Retrieves the details of a specific DNS Service matching the id of the Service. | id | Query: startTime, endTime |
| GET | `/dna/intent/api/v1/network-device/{id}/meraki-organization` | getOrganizationListForMeraki | Get Organization list for Meraki | id |
| GET | `/dna/intent/api/v1/interface/{interfaceUuid}/legit-operation` | legitOperationsForInterface | Legit operations for interface | interfaceUuid |
| GET | `/dna/intent/api/v1/network-device/{deviceUuid}/supervisor-card` | getSupervisorCardDetail | Get Supervisor card detail | deviceUuid |
| POST | `/dna/data/api/v1/dnsServices/query/count` | retrievesTheTotalNumberOfDNSServicesForGivenSetOfComplexFilters. | Retrieves the total number of DNS Services for given set of complex filters. |  |
| DELETE | `/dna/intent/api/v1/network-device/{deviceId}/user-defined-field` | removeUser-Defined-FieldFromDevice | Remove User-Defined-Field from device | deviceId | Query: name |
| PUT | `/dna/intent/api/v1/network-device/{deviceId}/user-defined-field` | addUser-Defined-FieldToDevice | Add User-Defined-Field to device | deviceId |
| GET | `/dna/intent/api/v1/networkDevices` | retrieveNetworkDevices | Retrieve network devices | Query: id, managementAddress, serialNumber, family, stackDevice, role, status, reachabilityStatus, managementState, views, limit, offset, sortBy, order |
| POST | `/dna/data/api/v1/dhcpServices/query` | retrievesTheListOfDHCPServicesForGivenSetOfComplexFilters. | Retrieves the list of DHCP Services for given set of complex filters. |  |
| POST | `/dna/data/api/v1/interfaces/query/count` | theTotalInterfacesCountAcrossTheNetworkDevices. | The Total interfaces count across the Network devices. |  |
| POST | `/dna/data/api/v1/dnsServices/topNAnalytics` | getTopNAnalyticsDataOfDNSServicesForGivenSetOfComplexFilters. | Get Top N analytics data of DNS Services for given set of complex filters. |  |
| POST | `/dna/intent/api/v1/networkDevices/deleteWithoutCleanup` | deleteANetworkDeviceWithoutConfigurationCleanup | Delete a network device without configuration cleanup |  |
| GET | `/dna/intent/api/v1/healthScoreDefinitions/{id}` | getHealthScoreDefinitionForTheGivenId. | Get health score definition for the given id. | id |
| PUT | `/dna/intent/api/v1/healthScoreDefinitions/{id}` | updateHealthScoreDefinitionForTheGivenId. | Update health score definition for the given id. | id |
| GET | `/dna/intent/api/v1/healthScoreDefinitions` | getAllHealthScoreDefinitionsForGivenFilters. | Get all health score definitions for given filters. | Query: deviceType, id, includeForOverallHealth, attribute, offset, limit |
| GET | `/dna/data/api/v1/interfaces` | getsInterfacesAlongWithStatisticsAndPoeDataFromAllNetworkDevices. | Gets interfaces along with statistics and poe data from all network devices. | Query: startTime, endTime, limit, offset, sortBy, order, siteHierarchy, siteHierarchyId, siteId, view, attribute, networkDeviceId, networkDeviceIpAddress, networkDeviceMacAddress, interfaceId, interfaceName |
| GET | `/dna/intent/api/v1/network-device/{deviceUuid}/interface/{interfaceUuid}/neighbor` | getConnectedDeviceDetail | Get connected device detail | deviceUuid, interfaceUuid |
| PUT | `/dna/intent/api/v1/network-device/{deviceid}/management-address` | updateDeviceManagementAddress | Update Device Management Address | deviceid |
| GET | `/dna/intent/api/v1/network-device/config` | getDeviceConfigForAllDevices | Get Device Config for all devices |  |
| PUT | `/dna/intent/api/v1/network-device/brief` | updateDeviceRole | Update Device role |  |
| GET | `/dna/intent/api/v1/buildings/{buildingId}/planned-access-points` | getPlannedAccessPointsForBuilding | Get Planned Access Points for Building | buildingId | Query: limit, offset, radios |
| GET | `/dna/data/api/v1/interfaces/{id}` | getTheInterfaceDataForTheGivenInterfaceId(instanceUuid)AlongWithTheStatisticsAndPoeData | Get the interface data for the given interface id (instance Uuid) along with the statistics and poe data | id | Query: startTime, endTime, view, attribute |
| GET | `/dna/intent/api/v1/interface/{id}` | getInterfaceById | Get Interface by Id | id |
| GET | `/dna/data/api/v1/networkDevices` | getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters. | Gets the Network Device details based on the provided query parameters. | Query: startTime, endTime, limit, offset, sortBy, order, siteHierarchy, siteHierarchyId, siteId, id, managementIpAddress, macAddress, family, type, role, serialNumber, maintenanceMode, softwareVersion, healthScore, view, attribute, fabricSiteId, l2Vn, l3Vn, transitNetworkId, fabricRole |
| GET | `/dna/data/api/v1/aaaServices` | retrievesTheListOfAAAServicesForGivenParameters. | Retrieves the list of AAA Services for given parameters. | Query: startTime, endTime, limit, offset, sortBy, order, serverIp, deviceId, deviceName, siteHierarchy, deviceSiteHierarchyId, siteId |
| GET | `/dna/intent/api/v1/interface/network-device/{deviceId}` | getInterfaceInfoById | Get Interface info by Id | deviceId |
| POST | `/dna/data/api/v1/assuranceEvents/query` | queryAssuranceEventsWithFilters | Query assurance events with filters |  |
| GET | `/dna/intent/api/v1/networkDevices/count` | countTheNumberOfNetworkDevices | Count the number of network devices | Query: id, managementAddress, serialNumber, family, stackDevice, role, status, reachabilityStatus, managementState |
| GET | `/dna/intent/api/v1/interface/ip-address/{ipAddress}` | getInterfaceByIP | Get Interface by IP | ipAddress |
| GET | `/dna/data/api/v1/dhcpServices` | retrievesTheListOfDHCPServicesForGivenParameters. | Retrieves the list of DHCP Services for given parameters. | Query: startTime, endTime, limit, offset, sortBy, order, serverIp, deviceId, deviceName, deviceSiteHierarchy, deviceSiteHierarchyId, deviceSiteId |
| POST | `/dna/data/api/v1/dhcpServices/topNAnalytics` | getTopNAnalyticsDataOfDHCPServicesForGivenSetOfComplexFilters. | Get Top N analytics data of DHCP Services for given set of complex filters. |  |
| GET | `/dna/intent/api/v1/network-device/functional-capability` | getFunctionalCapabilityForDevices | Get Functional Capability for devices | Query: deviceId, functionName |
| POST | `/dna/data/api/v1/energy/networkDevices/query/count` | countDevicesEnergyFromQuery | Count devices energy from query |  |
| GET | `/dna/intent/api/v1/network-device/serial-number/{serialNumber}` | getDeviceBySerialNumber | Get Device by Serial number | serialNumber |
| GET | `/dna/data/api/v1/aaaServices/count` | retrievesTheTotalNumberOfAAAServicesForGivenParameters. | Retrieves the total number of AAA Services for given parameters. | Query: startTime, endTime, serverIp, deviceId, deviceName, deviceSiteHierarchy, deviceSiteHierarchyId, deviceSiteId |
| POST | `/dna/data/api/v1/dhcpServices/{id}/trendAnalytics` | getTrendAnalyticsDataForAGivenDHCPServiceMatchingTheIdOfTheService. | Get trend analytics data for a given DHCP Service matching the id of the Service. | id |
| POST | `/dna/data/api/v1/dnsServices/query` | retrievesTheListOfDNSServicesForGivenSetOfComplexFilters. | Retrieves the list of DNS Services for given set of complex filters. |  |
| GET | `/dna/intent/api/v1/network-device/tenantinfo/macaddress` | getDevicesRegisteredForWSANotification | Get Devices registered for WSA Notification | Query: serialNumber, macaddress |
| GET | `/dna/data/api/v1/energy/networkDevices/{id}` | getDeviceEnergyByID | Get device energy by ID | id | Query: startTime, endTime, view, attribute |
| GET | `/dna/intent/api/v1/device-detail` | getDeviceDetail | Get Device Detail | Query: timestamp, identifier, searchBy |
| POST | `/dna/intent/api/v1/network-device/file` | exportDeviceList | Export Device list |  |
| GET | `/dna/intent/api/v1/network-device/ip-address/{ipAddress}` | getNetworkDeviceByIP | Get Network Device by IP | ipAddress |
| POST | `/dna/data/api/v1/assuranceEvents/query/count` | countTheNumberOfEventsWithFilters | Count the number of events with filters |  |
| GET | `/dna/data/api/v1/assuranceEvents/{id}/childEvents` | getListOfChildEventsForTheGivenWirelessClientEvent | Get list of child events for the given wireless client event | id |
| GET | `/dna/intent/api/v1/network-device/module` | getModules | Get Modules | Query: deviceId, limit, offset, nameList, vendorEquipmentTypeList, partNumberList, operationalStateCodeList |
| POST | `/dna/data/api/v1/interfaces/{id}/trendAnalytics` | theTrendAnalytcisDataForTheInterfacesInTheSpecifiedTimeRange | The Trend analytcis data for the interfaces in the specified time range | id |
| GET | `/dna/intent/api/v1/network-device/{id}/wireless-info` | getWirelessLanControllerDetailsById | Get wireless lan controller details by Id | id |
| POST | `/dna/data/api/v1/networkDevices/query` | getsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions. | Gets the list of Network Devices based on the provided complex filters and aggregation functions. |  |
| POST | `/dna/data/api/v1/dnsServices/trendAnalytics` | getTrendAnalyticsDataOfDNSServicesForGivenSetOfComplexFilters. | Get trend analytics data of DNS Services for given set of complex filters. |  |
| GET | `/dna/data/api/v1/networkDevices/count` | getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters. | Gets the total Network device counts based on the provided query parameters. | Query: startTime, endTime, id, siteHierarchy, siteHierarchyId, siteId, managementIpAddress, macAddress, family, type, role, serialNumber, maintenanceMode, softwareVersion, healthScore, fabricSiteId, l2Vn, l3Vn, transitNetworkId, fabricRole |
| POST | `/dna/data/api/v1/aaaServices/{id}/trendAnalytics` | getTrendAnalyticsDataForAGivenAAAServiceMatchingTheIdOfTheService. | Get trend analytics data for a given AAA Service matching the id of the Service. | id |
| GET | `/dna/intent/api/v1/network-device/{startIndex}/{recordsToReturn}` | getNetworkDeviceByPaginationRange | Get Network Device by pagination range | startIndex, recordsToReturn |
| POST | `/dna/data/api/v1/aaaServices/query/count` | retrievesTheTotalNumberOfAAAServicesForGivenSetOfComplexFilters. | Retrieves the total number of AAA Services for given set of complex filters. |  |
| GET | `/dna/intent/api/v1/interface` | getAllInterfaces | Get all interfaces | Query: offset, limit, lastInputTime, lastOutputTime |
| GET | `/dna/intent/api/v1/network-device/autocomplete` | getDeviceValuesThatMatchFullyOrPartiallyAnAttribute | Get Device Values that match fully or partially an Attribute | Query: vrfName, managementIpAddress, hostname, macAddress, family, collectionStatus, collectionInterval, softwareVersion, softwareType, reachabilityStatus, reachabilityFailureReason, errorCode, platformId, series, type, serialNumber, upTime, role, roleSource, associatedWlcIp, offset, limit |
| GET | `/dna/intent/api/v1/device-enrichment-details` | getDeviceEnrichmentDetails | Get Device Enrichment Details |  |

#### EoX

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/eox-status/device` | getEoXStatusForAllDevices | Get EoX Status For All Devices | Query: limit, offset |
| GET | `/dna/intent/api/v1/eox-status/device/{deviceId}` | getEoXDetailsPerDevice | Get EoX Details Per Device | deviceId |
| GET | `/dna/intent/api/v1/eox-status/summary` | getEoXSummary | Get EoX Summary |  |

#### Issues

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/data/api/v1/assuranceIssues/count` | getTheTotalNumberOfIssuesForGivenSetOfFilters | Get the total number of issues for given set of filters | Query: startTime, endTime, isGlobal, priority, severity, status, entityType, category, deviceType, name, issueId, entityId, updatedBy, siteHierarchy, siteHierarchyId, siteName, siteId, fabricSiteId, fabricVnName, fabricTransitSiteId, networkDeviceId, networkDeviceIpAddress, macAddress, aiDriven, fabricDriven, fabricSiteDriven, fabricVnDriven, fabricTransitDriven |
| PUT | `/dna/intent/api/v1/systemIssueDefinitions/{id}` | issueTriggerDefinitionUpdate. | Issue trigger definition update. | id |
| GET | `/dna/intent/api/v1/systemIssueDefinitions/{id}` | getIssueTriggerDefinitionForGivenId. | Get issue trigger definition for given id. | id |
| GET | `/dna/intent/api/v1/customIssueDefinitions` | getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters. | Get all the custom issue definitions based on the given filters. | Query: id, profileId, name, priority, isEnabled, severity, facility, mnemonic, limit, offset, sortBy, order |
| POST | `/dna/intent/api/v1/customIssueDefinitions` | createsANewUser-definedIssueDefinitions. | Creates a new user-defined issue definitions. |  |
| POST | `/dna/data/api/v1/assuranceIssues/topNAnalytics` | getTopNAnalyticsDataOfIssues | Get Top N analytics data of issues |  |
| GET | `/dna/intent/api/v1/systemIssueDefinitions` | returnsAllIssueTriggerDefinitionsForGivenFilters. | Returns all issue trigger definitions for given filters. | Query: deviceType, profileId, id, name, priority, issueEnabled, attribute, offset, limit, sortBy, order |
| POST | `/dna/intent/api/v1/assuranceIssues/ignore` | ignoreTheGivenListOfIssues | Ignore the given list of issues |  |
| POST | `/dna/data/api/v1/assuranceIssues/query` | getTheDetailsOfIssuesForGivenSetOfFilters | Get the details of issues for given set of filters |  |
| GET | `/dna/data/api/v1/assuranceIssues/{id}` | getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId | Get all the details and suggested actions of an issue for the given issue id | id | Query: view, attribute |
| PUT | `/dna/intent/api/v1/customIssueDefinitions/{id}` | updatesAnExistingCustomIssueDefinitionBasedOnTheProvidedId. | Updates an existing custom issue definition based on the provided Id. | id |
| GET | `/dna/intent/api/v1/customIssueDefinitions/{id}` | getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId. | Get the custom issue definition for the given custom issue definition Id. | id |
| DELETE | `/dna/intent/api/v1/customIssueDefinitions/{id}` | deletesAnExistingCustomIssueDefinition. | Deletes an existing custom issue definition. | id |
| GET | `/dna/intent/api/v1/customIssueDefinitions/count` | getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters. | Get the total custom issue definitions count based on the provided filters. | Query: id, profileId, name, priority, isEnabled, severity, facility, mnemonic |
| GET | `/dna/intent/api/v1/systemIssueDefinitions/count` | getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters. | Get the count of system defined issue definitions based on provided filters. | Query: deviceType, profileId, id, name, priority, issueEnabled |
| GET | `/dna/data/api/v1/assuranceIssues` | getTheDetailsOfIssuesForGivenSetOfFilters-2 | Get the details of issues for given set of filters | Query: startTime, endTime, limit, offset, sortBy, order, isGlobal, priority, severity, status, entityType, category, deviceType, name, issueId, entityId, updatedBy, siteHierarchy, siteHierarchyId, siteName, siteId, fabricSiteId, fabricVnName, fabricTransitSiteId, networkDeviceId, networkDeviceIpAddress, macAddress, view, attribute, aiDriven, fabricDriven, fabricSiteDriven, fabricVnDriven, fabricTransitDriven |
| POST | `/dna/data/api/v1/assuranceIssues/query/count` | getTheTotalNumberOfIssuesForGivenSetOfFilters-2 | Get the total number of issues for given set of filters |  |
| POST | `/dna/intent/api/v1/assuranceIssues/{id}/update` | updateTheGivenIssueByUpdatingSelectedFields | Update the given issue by updating selected fields | id |
| POST | `/dna/data/api/v1/assuranceIssues/summaryAnalytics` | getSummaryAnalyticsDataOfIssues | Get summary analytics data of issues |  |
| POST | `/dna/intent/api/v1/assuranceIssues/resolve` | resolveTheGivenListsOfIssues | Resolve the given lists of issues |  |
| GET | `/dna/intent/api/v1/issues` | issues | Issues | Query: startTime, endTime, siteId, deviceId, macAddress, priority, issueStatus, aiDriven |
| POST | `/dna/data/api/v1/assuranceIssues/trendAnalytics` | getTrendAnalyticsDataOfIssues | Get trend analytics data of issues |  |
| GET | `/dna/intent/api/v1/issue-enrichment-details` | getIssueEnrichmentDetails | Get Issue Enrichment Details |  |
| POST | `/dna/intent/api/v1/execute-suggested-actions-commands` | executeSuggestedActionsCommands | Execute Suggested Actions Commands |  |

#### Security Advisories

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/security-advisory/device/{deviceId}/advisory` | getAdvisoriesPerDevice | Get Advisories Per Device | deviceId |
| GET | `/dna/intent/api/v1/security-advisory/advisory/aggregate` | getAdvisoriesSummary | Get Advisories Summary |  |
| GET | `/dna/intent/api/v1/security-advisory/advisory` | getAdvisoriesList | Get Advisories List |  |
| GET | `/dna/intent/api/v1/security-advisory/device/{deviceId}` | getAdvisoryDeviceDetail | Get Advisory Device Detail | deviceId |
| GET | `/dna/intent/api/v1/security-advisory/advisory/{advisoryId}/device` | getDevicesPerAdvisory | Get Devices Per Advisory | advisoryId |

#### Sensors

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| DELETE | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}` | discardsTheICAPConfigurationIntentByActivityID. | Discards the ICAP configuration intent by activity ID. | previewActivityId |
| GET | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config` | retrievesTheDevice'sCLIsOfTheICAPIntent. | Retrieves the device's CLIs of the ICAP intent. | previewActivityId, networkDeviceId |
| POST | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config` | generatesTheDevice'sCLIsOfTheICAPConfigurationIntent. | Generates the device's CLIs of the ICAP configuration intent. | previewActivityId, networkDeviceId |
| GET | `/dna/intent/api/v1/icapSettings/count` | retrievesTheCountOfDeployedICAPConfigurationsWhileSupportingBasicFiltering. | Retrieves the count of deployed ICAP configurations while supporting basic filtering. | Query: captureType, captureStatus, clientMac, apId, wlcId |
| GET | `/dna/data/api/v1/icap/captureFiles/{id}/download` | downloadsASpecificICAPPacketCaptureFile | Downloads a specific ICAP packet capture file | id |
| GET | `/dna/data/api/v1/icap/captureFiles/count` | retrievesTheTotalNumberOfPacketCaptureFilesMatchingSpecifiedCriteria | Retrieves the total number of packet capture files matching specified criteria | Query: type, clientMac, apMac, startTime, endTime |
| GET | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDeviceStatusDetails` | getICAPConfigurationStatusPerNetworkDevice. | Get ICAP configuration status per network device. | previewActivityId |
| GET | `/dna/intent/api/v1/icapSettings/deviceDeployments` | getDeviceDeploymentStatus. | Get device deployment status. | Query: deployActivityId, networkDeviceIds, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/icapSettings/deviceDeployments/count` | getDeviceDeploymentStatusCount. | Get device deployment status count. | Query: deployActivityId, networkDeviceIds |
| POST | `/dna/intent/api/v1/icapSettings/deploy` | deploysTheGivenICAPConfigurationIntentWithoutPreviewAndApprove. | Deploys the given ICAP configuration intent without preview and approve. | Query: previewDescription |
| POST | `/dna/intent/api/v1/icapSettings/deploy/{id}/deleteDeploy` | removeTheICAPConfigurationOnTheDeviceWithoutPreview | Remove the ICAP configuration on the device without preview | id |
| GET | `/dna/data/api/v1/icap/spectrumInterferenceDeviceReports` | retrievesTheSpectrumInterferenceDevicesReportsSentByWLCForProvidedAPMac | Retrieves the spectrum interference devices reports sent by WLC for provided AP Mac | Query: startTime, endTime, apMac, limit, offset, timeSortOrder |
| GET | `/dna/data/api/v1/icap/captureFiles/{id}` | retrievesDetailsOfASpecificICAPPacketCaptureFile | Retrieves details of a specific ICAP packet capture file | id |
| POST | `/dna/data/api/v1/icap/radios/{id}/stats` | retrievesSpecificRadioStatisticsOverSpecifiedPeriodOfTime. | Retrieves specific radio statistics over specified period of time. | id |
| POST | `/dna/data/api/v1/icap/clients/{id}/stats` | retrievesSpecificClientStatisticsOverSpecifiedPeriodOfTime. | Retrieves specific client statistics over specified period of time. | id |
| GET | `/dna/data/api/v1/icap/captureFiles` | listsICAPPacketCaptureFilesMatchingSpecifiedCriteria | Lists ICAP packet capture files matching specified criteria | Query: type, clientMac, apMac, startTime, endTime, limit, offset, sortBy, order |
| POST | `/dna/intent/api/v1/icapSettings/configurationModels` | createsAnICAPConfigurationIntentForPreview-approve. | Creates an ICAP configuration intent for preview-approve. | Query: previewDescription |
| GET | `/dna/intent/api/v1/icapSettings` | retrievesDeployedICAPConfigurationsWhileSupportingBasicFiltering. | Retrieves deployed ICAP configurations while supporting basic filtering. | Query: captureStatus, captureType, clientMac, apId, wlcId, offset, limit |
| POST | `/dna/intent/api/v1/icapSettings/configurationModels/{id}/deleteDeploy` | createsAICAPConfigurationWorkflowForICAPIntentToRemoveTheICAPConfigurationOnTheDevice. | Creates a ICAP configuration workflow for ICAP intent to remove the ICAP configuration on the device. | id |
| POST | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/deploy` | deploysTheICAPConfigurationIntentByActivityID. | Deploys the ICAP configuration intent by activity ID. | previewActivityId |
| GET | `/dna/data/api/v1/icap/spectrumSensorReports` | retrievesTheSpectrumSensorReportsSentByWLCForProvidedAPMac | Retrieves the spectrum sensor reports sent by WLC for provided AP Mac | Query: startTime, endTime, apMac, dataType, limit, offset, timeSortOrder |
| POST | `/dna/intent/api/v1/sensor` | createSensorTestTemplate | Create sensor test template |  |
| GET | `/dna/intent/api/v1/sensor` | sensors | Sensors | Query: siteId |
| DELETE | `/dna/intent/api/v1/sensor` | deleteSensorTest | Delete sensor test | Query: templateName |
| PUT | `/dna/intent/api/v1/sensorTestTemplate` | duplicateSensorTestTemplate | Duplicate sensor test template |  |
| PUT | `/dna/intent/api/v1/AssuranceScheduleSensorTest` | editSensorTestTemplate | Edit sensor test template |  |
| PUT | `/dna/intent/api/v1/sensor-run-now` | runNowSensorTest | Run now sensor test |  |

#### Sites

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/data/api/v1/energy/sites/query/count` | submitRequestToCountSitesEnergyFromQuery | Submit request to count sites energy from query | Query: taskId |
| GET | `/dna/data/api/v1/energy/sites/query/count` | countSitesEnergyForTheGivenTaskID | Count sites energy for the given task ID | Query: taskId |
| GET | `/dna/intent/api/v1/site-health` | getSiteHealth | Get Site Health | Query: siteType, offset, limit, timestamp |
| POST | `/dna/data/api/v1/siteHealthSummaries/summaryAnalytics` | queryAnAggregatedSummaryOfSiteHealthData. | Query an aggregated summary of site health data. | Query: siteHierarchy, siteHierarchyId, siteType, id |
| GET | `/dna/data/api/v1/siteHealthSummaries/summaryAnalytics` | readAnAggregatedSummaryOfSiteHealthData. | Read an aggregated summary of site health data. | Query: startTime, endTime, siteHierarchy, siteHierarchyId, siteType, id, view, attribute |
| POST | `/dna/data/api/v1/siteKpiSummaries/trendAnalytics` | submitRequestForSiteAnalyticsTrendData | Submit request for site analytics trend data |  |
| GET | `/dna/data/api/v1/siteKpiSummaries/trendAnalytics` | getSiteAnalyticsTrendDataForTheGivenTaskId | Get site analytics trend data for the given task id | Query: taskId |
| GET | `/dna/intent/api/v2/site/count` | getSiteCountV2 | Get Site Count V2 | Query: id |
| POST | `/dna/data/api/v1/siteKpiSummaries/query` | getSiteAnalyticsForTheChildSitesOfGivenParentSiteAndOtherFilters. | Get site analytics for the child sites of given parent site and other filters. |  |
| GET | `/dna/data/api/v1/siteHealthSummaries/{id}` | readSiteHealthSummaryDataBySiteId. | Read site health summary data by site id. | id | Query: startTime, endTime, view, attribute |
| POST | `/dna/data/api/v1/siteKpiSummaries/topNAnalytics` | submitRequestForTopNEntitiesRelatedToSiteAnalytics | Submit request for Top N entities related to site analytics |  |
| GET | `/dna/data/api/v1/siteKpiSummaries/topNAnalytics` | getTopNEntitiesRelatedToSiteAnalyticsForTheGivenTaskId | Get Top N entities related to site analytics for the given task id | Query: taskId |
| GET | `/dna/data/api/v1/energy/sites` | getSitesEnergy | Get sites energy | Query: startTime, endTime, limit, offset, sortBy, order, siteHierarchy, siteHierarchyId, siteName, siteType, deviceCategory, siteId, views, attribute, taskId |
| POST | `/dna/intent/api/v1/maps/import/{importContextUuid}/perform` | importMapArchive-PerformImport | Import Map Archive - Perform Import | importContextUuid |
| DELETE | `/dna/intent/api/v1/maps/import/{importContextUuid}` | importMapArchive-CancelAnImport | Import Map Archive - Cancel an Import | importContextUuid |
| GET | `/dna/data/api/v1/siteKpiSummaries/{id}` | getSiteAnalyticsForOneSite. | Get site analytics for one site. | id | Query: taskId, startTime, endTime, ssid, band, failureCategory, failureReason, view, attribute |
| GET | `/dna/intent/api/v2/site` | getSiteV2 | Get Site V2 | Query: groupNameHierarchy, id, type, offset, limit |
| GET | `/dna/data/api/v1/energy/sites/{id}` | getSiteEnergyByID | Get site energy by ID | id | Query: startTime, endTime, views, attribute, deviceCategory, taskId |
| GET | `/dna/data/api/v1/siteHealthSummaries/trendAnalytics` | readTrendAnalyticsDataForAGroupingOfSitesInYourNetwork | Read trend analytics data for a grouping of sites in your network | Query: startTime, endTime, siteHierarchy, siteHierarchyId, siteType, id, trendInterval, limit, offset, timeSortOrder, attribute, taskId |
| POST | `/dna/data/api/v1/energy/sites/query` | submitRequestToQuerySitesEnergy | Submit request to query sites energy | Query: taskId |
| GET | `/dna/data/api/v1/energy/sites/query` | querySitesEnergyForTheGivenTaskID | Query sites energy for the given task ID | Query: taskId |
| GET | `/dna/intent/api/v1/maps/supported-access-points` | mapsSupportedAccessPoints | Maps Supported Access Points |  |
| GET | `/dna/data/api/v1/siteKpiSummaries/summaryAnalytics` | getSiteAnalyticsSummaryDataForTheGivenTaskId | Get site analytics summary data for the given task id | Query: taskId |
| POST | `/dna/data/api/v1/siteKpiSummaries/summaryAnalytics` | submitRequestForSiteAnalyticsSummaryData | Submit request for site analytics summary data |  |
| GET | `/dna/intent/api/v1/site-member/{id}/member` | getDevicesThatAreAssignedToASite | Get devices that are assigned to a site | id | Query: offset, limit, memberType, level |
| POST | `/dna/intent/api/v1/maps/import/start` | importMapArchive-StartImport | Import Map Archive - Start Import |  |
| GET | `/dna/data/api/v1/siteHealthSummaries/count` | readSiteCount. | Read site count. | Query: endTime, siteHierarchy, siteHierarchyId, siteType, id |
| GET | `/dna/data/api/v1/siteKpiSummaries/count` | getTheTotalNumberOfSiteAnalyticsRecordsAvailableForForGivenSetOfQueryParameters. | Get the total number of site analytics records available for for given set of query parameters. | Query: startTime, endTime, siteHierarchy, siteHierarchyId, siteId, siteType |
| GET | `/dna/data/api/v1/energy/sites/count` | countSitesEnergy | Count sites energy | Query: startTime, endTime, siteHierarchy, siteHierarchyId, siteName, siteType, deviceCategory, siteId, taskId |
| GET | `/dna/intent/api/v1/maps/import/{importContextUuid}/status` | importMapArchive-ImportStatus | Import Map Archive - Import Status | importContextUuid |
| GET | `/dna/data/api/v1/siteHealthSummaries/{id}/trendAnalytics` | readTrendAnalyticsDataForASpecificSiteInYourNetwork | Read trend analytics data for a specific site in your network | id | Query: startTime, endTime, trendInterval, limit, offset, timeSortOrder, attribute, taskId |
| GET | `/dna/data/api/v1/siteHealthSummaries` | readListOfSiteHealthSummaries. | Read list of site health summaries. | Query: startTime, endTime, limit, offset, sortBy, order, siteHierarchy, siteHierarchyId, siteType, id, view, attribute |
| GET | `/dna/data/api/v1/siteKpiSummaries` | getSiteAnalyticsForTheChildSitesOfGivenParentSiteAndOtherQueryParameters. | Get site analytics for the child sites of given parent site and other query parameters. | Query: taskId, startTime, endTime, siteHierarchy, siteHierarchyId, siteId, siteType, ssid, band, failureCategory, failureReason, view, attribute, limit, offset, sortBy, order |
| POST | `/dna/data/api/v1/siteKpiSummaries/query/count` | getTheTotalNumberOfSiteAnalyticsRecordsAvailableForForGivenSetOfFilters. | Get the total number of site analytics records available for for given set of filters. |  |
| POST | `/dna/intent/api/v1/maps/export/{siteHierarchyUuid}` | exportMapArchive | Export Map Archive | siteHierarchyUuid |
| POST | `/dna/intent/api/v1/assign-device-to-site/{siteId}/device` | assignDevicesToSite | Assign Devices To Site | siteId |
| POST | `/dna/intent/api/v1/site` | createSite | Create Site |  |
| GET | `/dna/intent/api/v1/site` | getSite | Get Site | Query: name, siteId, type, offset, limit |
| DELETE | `/dna/intent/api/v1/site/{siteId}` | deleteSite | Delete Site | siteId |
| PUT | `/dna/intent/api/v1/site/{siteId}` | updateSite | Update Site | siteId |
| GET | `/dna/intent/api/v1/site/count` | getSiteCount | Get Site Count | Query: siteId |
| GET | `/dna/intent/api/v1/membership/{siteId}` | getMembership | Get Membership | siteId | Query: offset, limit, deviceFamily, serialNumber |

#### Topology

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/topology/vlan/vlan-names` | getVLANDetails | Get VLAN details |  |
| GET | `/dna/intent/api/v1/network-health` | getOverallNetworkHealth | Get Overall Network Health | Query: timestamp |
| GET | `/dna/intent/api/v1/topology/site-topology` | getSiteTopology | Get Site Topology |  |
| GET | `/dna/intent/api/v1/topology/physical-topology` | getPhysicalTopology | Get Physical Topology | Query: nodeType |
| GET | `/dna/intent/api/v1/topology/l2/{vlanID}` | getTopologyDetails | Get topology details | vlanID |
| GET | `/dna/intent/api/v1/topology/l3/{topologyType}` | getL3TopologyDetails | Get L3 Topology Details | topologyType |

#### Users

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/user-enrichment-details` | getUserEnrichmentDetails | Get User Enrichment Details |  |

### Operational Tasks

#### Command Runner

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/network-device-poller/cli/legit-reads` | getAllKeywordsOfCLIsAcceptedByCommandRunner | Get all keywords of CLIs accepted by command runner |  |
| POST | `/dna/intent/api/v1/network-device-poller/cli/read-request` | runRead-onlyCommandsOnDevicesToGetTheirReal-timeConfiguration | Run read-only commands on devices to get their real-time configuration |  |

#### Discovery

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/discovery/count` | getCountOfAllDiscoveryJobs | Get count of all discovery jobs |  |
| POST | `/dna/intent/api/v1/global-credential/netconf` | createNetconfCredentials | Create Netconf credentials |  |
| PUT | `/dna/intent/api/v1/global-credential/netconf` | updateNetconfCredentials | Update Netconf credentials |  |
| PUT | `/dna/intent/api/v1/global-credential/snmpv2-write-community` | updateSNMPWriteCommunity | Update SNMP write community |  |
| POST | `/dna/intent/api/v1/global-credential/snmpv2-write-community` | createSNMPWriteCommunity | Create SNMP write community |  |
| PUT | `/dna/intent/api/v1/global-credential/snmpv3` | updateSNMPv3Credentials | Update SNMPv3 credentials |  |
| POST | `/dna/intent/api/v1/global-credential/snmpv3` | createSNMPv3Credentials | Create SNMPv3 credentials |  |
| GET | `/dna/intent/api/v1/discovery/{startIndex}/{recordsToReturn}` | getDiscoveriesByRange | Get Discoveries by range | startIndex, recordsToReturn |
| GET | `/dna/intent/api/v1/discovery/{id}/summary` | getNetworkDevicesFromDiscovery | Get network devices from Discovery | id | Query: taskId, sortBy, sortOrder, ipAddress, pingStatus, snmpStatus, cliStatus, netconfStatus, httpStatus |
| GET | `/dna/intent/api/v1/snmp-property` | getSNMPProperties | Get SNMP properties |  |
| POST | `/dna/intent/api/v1/snmp-property` | create/UpdateSNMPProperties | Create/Update SNMP properties |  |
| PUT | `/dna/intent/api/v1/global-credential/snmpv2-read-community` | updateSNMPReadCommunity | Update SNMP read community |  |
| POST | `/dna/intent/api/v1/global-credential/snmpv2-read-community` | createSNMPReadCommunity | Create SNMP read community |  |
| DELETE | `/dna/intent/api/v1/discovery/{id}` | deleteDiscoveryById | Delete discovery by Id | id |
| GET | `/dna/intent/api/v1/discovery/{id}` | getDiscoveryById | Get Discovery by Id | id |
| POST | `/dna/intent/api/v2/global-credential` | createGlobalCredentialsV2 | Create Global Credentials V2 |  |
| GET | `/dna/intent/api/v2/global-credential` | getAllGlobalCredentialsV2 | Get All Global Credentials V2 |  |
| PUT | `/dna/intent/api/v2/global-credential` | updateGlobalCredentialsV2 | Update Global Credentials V2 |  |
| POST | `/dna/intent/api/v1/global-credential/http-write` | createHTTPWriteCredentials | Create HTTP write credentials |  |
| PUT | `/dna/intent/api/v1/global-credential/http-write` | updateHTTPWriteCredentials | Update HTTP write credentials |  |
| POST | `/dna/intent/api/v1/discovery` | startDiscovery | Start discovery |  |
| PUT | `/dna/intent/api/v1/discovery` | updatesAnExistingDiscoveryBySpecifiedId | Updates an existing discovery by specified Id |  |
| DELETE | `/dna/intent/api/v1/discovery` | deleteAllDiscovery | Delete all discovery |  |
| DELETE | `/dna/intent/api/v2/global-credential/{id}` | deleteGlobalCredentialV2 | Delete Global Credential V2 | id |
| PUT | `/dna/intent/api/v1/global-credential/{globalCredentialId}` | updateGlobalCredentials | Update global credentials | globalCredentialId |
| DELETE | `/dna/intent/api/v1/global-credential/{globalCredentialId}` | deleteGlobalCredentialsById | Delete global credentials by Id | globalCredentialId |
| PUT | `/dna/intent/api/v1/global-credential/http-read` | updateHTTPReadCredential | Update HTTP read credential |  |
| POST | `/dna/intent/api/v1/global-credential/http-read` | createHTTPReadCredentials | Create HTTP read credentials |  |
| GET | `/dna/intent/api/v1/discovery/{id}/job` | getListOfDiscoveriesByDiscoveryId | Get list of discoveries by discovery Id | id | Query: offset, limit, ipAddress |
| POST | `/dna/intent/api/v1/global-credential/cli` | createCLICredentials | Create CLI credentials |  |
| PUT | `/dna/intent/api/v1/global-credential/cli` | updateCLICredentials | Update CLI credentials |  |
| GET | `/dna/intent/api/v1/discovery/job` | getDiscoveryJobsByIP | Get Discovery jobs by IP | Query: offset, limit, ipAddress, name |
| GET | `/dna/intent/api/v1/discovery/{id}/network-device/count` | getDevicesDiscoveredById | Get Devices discovered by Id | id | Query: taskId |
| GET | `/dna/intent/api/v1/discovery/{id}/network-device/{startIndex}/{recordsToReturn}` | getDiscoveredDevicesByRange | Get Discovered devices by range | id, startIndex, recordsToReturn | Query: taskId |
| GET | `/dna/intent/api/v1/global-credential` | getGlobalCredentials | Get Global credentials | Query: credentialSubType, sortBy, order |
| GET | `/dna/intent/api/v1/discovery/{id}/network-device` | getDiscoveredNetworkDevicesByDiscoveryId | Get Discovered network devices by discovery Id | id | Query: taskId |

#### File

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/file/{nameSpace}` | uploadFile | uploadFile | nameSpace |
| GET | `/dna/intent/api/v1/file/namespace` | getListOfAvailableNamespaces | Get list of available namespaces |  |
| GET | `/dna/intent/api/v1/file/namespace/{nameSpace}` | getListOfFiles | Get list of files | nameSpace |
| GET | `/dna/intent/api/v1/file/{fileId}` | downloadAFileByFileId | Download a file by fileId | fileId |

#### Path Trace

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/flow-analysis` | retrievesAllPreviousPathtracesSummary | Retrieves all previous Pathtraces summary | Query: periodicRefresh, sourceIP, destIP, sourcePort, destPort, gtCreateTime, ltCreateTime, protocol, status, taskId, lastUpdateTime, limit, offset, order, sortBy |
| POST | `/dna/intent/api/v1/flow-analysis` | initiateANewPathtrace | Initiate a new Pathtrace |  |
| GET | `/dna/intent/api/v1/flow-analysis/{flowAnalysisId}` | retrievesPreviousPathtrace | Retrieves previous Pathtrace | flowAnalysisId |
| DELETE | `/dna/intent/api/v1/flow-analysis/{flowAnalysisId}` | deletesPathtraceById | Deletes Pathtrace by Id | flowAnalysisId |

#### Reports

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/data/view-groups/{viewGroupId}` | getViewsForAGivenViewGroup | Get views for a given view group | viewGroupId |
| GET | `/dna/intent/api/v1/data/view-groups/{viewGroupId}/views/{viewId}` | getViewDetailsForAGivenViewGroup&View | Get view details for a given view group & view | viewGroupId, viewId |
| DELETE | `/dna/intent/api/v1/data/reports/{reportId}` | deleteAScheduledReport | Delete a scheduled report | reportId |
| GET | `/dna/intent/api/v1/data/reports/{reportId}` | getAScheduledReport | Get a scheduled report | reportId |
| GET | `/dna/data/api/v1/flexible-report/schedule/{reportId}` | getFlexibleReportScheduleByReportId | Get flexible report schedule by report id | reportId |
| PUT | `/dna/data/api/v1/flexible-report/schedule/{reportId}` | updateScheduleOfFlexibleReport | Update schedule of flexible report | reportId |
| GET | `/dna/intent/api/v1/data/view-groups` | getAllViewGroups | Get all view groups |  |
| GET | `/dna/intent/api/v1/data/reports` | getListOfScheduledReports | Get list of scheduled reports | Query: viewGroupId, viewId |
| POST | `/dna/intent/api/v1/data/reports` | createOrScheduleAReport | Create or Schedule a report |  |
| GET | `/dna/data/api/v1/flexible-report/report/{reportId}/executions` | getExecutionIdByReportId | Get Execution Id by Report Id | reportId |
| POST | `/dna/data/api/v1/flexible-report/report/{reportId}/execute` | executingTheFlexibleReport | Executing the Flexible report | reportId |
| GET | `/dna/data/api/v1/flexible-report/schedules` | getAllFlexibleReportSchedules | Get all flexible report schedules |  |
| GET | `/dna/intent/api/v1/data/reports/{reportId}/executions` | getAllExecutionDetailsForAGivenReport | Get all execution details for a given report | reportId |
| GET | `/dna/data/api/v1/flexible-report/report/content/{reportId}/{executionId}` | downloadFlexibleReport | Download Flexible Report | reportId, executionId |
| GET | `/dna/intent/api/v1/data/reports/{reportId}/executions/{executionId}` | downloadReportContent | Download report content | reportId, executionId |

#### Tag

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/tag/{id}/member` | addMembersToTheTag | Add members to the tag | id |
| GET | `/dna/intent/api/v1/tag/{id}/member` | getTagMembersById | Get Tag members by Id | id | Query: memberType, offset, limit, memberAssociationType, level |
| GET | `/dna/intent/api/v1/tags/networkDevices/membersAssociations` | retrieveTagsAssociatedWithNetworkDevices. | Retrieve tags associated with network devices. | Query: offset, limit |
| PUT | `/dna/intent/api/v1/tags/networkDevices/membersAssociations/bulk` | updateTagsAssociatedWithTheNetworkDevices. | Update tags associated with the network devices. |  |
| POST | `/dna/intent/api/v1/tag` | createTag | Create Tag |  |
| PUT | `/dna/intent/api/v1/tag` | updateTag | Update Tag |  |
| GET | `/dna/intent/api/v1/tag` | getTag | Get Tag | Query: name, additionalInfo.nameSpace, additionalInfo.attributes, level, offset, limit, size, field, sortBy, order, systemTag |
| GET | `/dna/intent/api/v1/tag/{id}/member/count` | getTagMemberCount | Get Tag Member count | id | Query: memberType, memberAssociationType |
| GET | `/dna/intent/api/v1/tags/interfaces/membersAssociations/count` | retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag. | Retrieve the count of interfaces that are associated with at least one tag. |  |
| DELETE | `/dna/intent/api/v1/tag/{id}` | deleteTag | Delete Tag | id |
| GET | `/dna/intent/api/v1/tag/{id}` | getTagById | Get Tag by Id | id |
| GET | `/dna/intent/api/v1/tag/member/type` | getTagResourceTypes | Get Tag resource types |  |
| PUT | `/dna/intent/api/v1/tag/member` | updateTagMembership | Update tag membership |  |
| POST | `/dna/intent/api/v1/tags/networkDevices/membersAssociations/query` | queryTheTagsAssociatedWithNetworkDevices. | Query the tags associated with network devices. |  |
| GET | `/dna/intent/api/v1/tags/networkDevices/membersAssociations/count` | retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag. | Retrieve the count of network devices that are associated with at least one tag. |  |
| GET | `/dna/intent/api/v1/tag/count` | getTagCount | Get Tag Count | Query: name, nameSpace, attributeName, size, systemTag |
| POST | `/dna/intent/api/v1/tags/interfaces/membersAssociations/query` | queryTheTagsAssociatedWithInterfaces. | Query the tags associated with interfaces. |  |
| PUT | `/dna/intent/api/v1/tags/interfaces/membersAssociations/bulk` | updateTagsAssociatedWithTheInterfaces. | Update tags associated with the interfaces. |  |
| GET | `/dna/intent/api/v1/tags/interfaces/membersAssociations` | retrieveTagsAssociatedWithTheInterfaces. | Retrieve tags associated with the interfaces. | Query: offset, limit |
| DELETE | `/dna/intent/api/v1/tag/{id}/member/{memberId}` | removeTagMember | Remove Tag member | id, memberId |

#### Task

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/data/api/v1/assuranceTasks/{id}` | retrieveASpecificAssuranceTaskById | Retrieve a specific assurance task by id | id |
| GET | `/dna/intent/api/v1/task/count` | getTaskCount | Get task count | Query: startTime, endTime, data, errorCode, serviceType, username, progress, isError, failureReason, parentId |
| GET | `/dna/intent/api/v1/tasks/{id}/detail` | getTaskDetailsByID | Get task details by ID | id |
| GET | `/dna/intent/api/v1/activities/{activityId}/triggeredJobs` | getTriggeredJobsByActivityId. | Get triggered jobs by activity id. | activityId | Query: offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/tasks/count` | getTasksCount | Get tasks count | Query: startTime, endTime, parentId, rootId, status |
| GET | `/intent/api/v1/activities/{id}` | getActivityByID. | Get activity by ID. | id |
| GET | `/dna/intent/api/v1/task/{taskId}` | getTaskById | Get task by Id | taskId |
| GET | `/dna/intent/api/v1/activities/count` | retrievesTheCountOfActivities | Retrieves the count of activities | Query: description, status, type, recurring, startTime, endTime |
| GET | `/dna/intent/api/v1/activities` | getActivities | Get activities | Query: description, status, type, recurring, startTime, endTime, offset, limit, sortBy, order |
| GET | `/dna/data/api/v1/assuranceTasks/count` | retrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExist | Retrieve a count of the number of assurance tasks that currently exist | Query: status |
| GET | `/dna/intent/api/v1/dnacaap/management/execution-status/{executionId}` | getBusinessAPIExecutionDetails | Get Business API Execution Details | executionId |
| GET | `/dna/intent/api/v1/tasks` | getTasks | Get tasks | Query: offset, limit, sortBy, order, startTime, endTime, parentId, rootId, status |
| GET | `/dna/intent/api/v1/task/operation/{operationId}/{offset}/{limit}` | getTaskByOperationId | Get task by OperationId | operationId, offset, limit |
| GET | `/dna/intent/api/v1/activities/{activityId}/triggeredJobs/count` | retrievesTheCountOfTriggeredJobsByActivityId. | Retrieves the count of triggered jobs by activity id. | activityId |
| GET | `/dna/data/api/v1/assuranceTasks` | retrieveAListOfAssuranceTasks | Retrieve a list of assurance tasks | Query: limit, offset, sortBy, order, status |
| GET | `/dna/intent/api/v1/tasks/{id}` | getTasksByID | Get tasks by ID | id |
| GET | `/dna/intent/api/v1/task` | getTasks-2 | Get tasks | Query: startTime, endTime, data, errorCode, serviceType, username, progress, isError, failureReason, parentId, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/task/{taskId}/tree` | getTaskTree | Get task tree | taskId |

### Policy

#### AI Endpoint Analytics

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId}` | getDetailsOfASingleProfilingRule | Get details of a single profiling rule | ruleId |
| PUT | `/dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId}` | updateAnExistingProfilingRule | Update an existing profiling rule | ruleId |
| DELETE | `/dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId}` | deleteAnExistingProfilingRule | Delete an existing profiling rule | ruleId |
| GET | `/dna/intent/api/v1/endpoint-analytics/endpoints/count` | fetchTheCountOfEndpoints | Fetch the count of endpoints | Query: profilingStatus, macAddress, macAddresses, ip, deviceType, hardwareManufacturer, hardwareModel, operatingSystem, registered, randomMac, trustScore, authMethod, postureStatus, aiSpoofingTrustLevel, changedProfileTrustLevel, natTrustLevel, concurrentMacTrustLevel, ipBlocklistDetected, unauthPortDetected, weakCredDetected, ancPolicy |
| GET | `/dna/intent/api/v1/endpoint-analytics/profiling-rules` | getListOfProfilingRules | Get list of profiling rules | Query: ruleType, includeDeleted, limit, offset, sortBy, order |
| POST | `/dna/intent/api/v1/endpoint-analytics/profiling-rules` | createAProfilingRule | Create a profiling rule |  |
| GET | `/dna/intent/api/v1/endpoint-analytics/tasks/{taskId}` | getTaskDetails | Get task details | taskId |
| GET | `/dna/intent/api/v1/endpoint-analytics/profiling-rules/count` | getCountOfProfilingRules | Get count of profiling rules | Query: ruleType, includeDeleted |
| DELETE | `/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}` | deleteAnEndpoint | Delete an endpoint | epId |
| GET | `/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}` | getEndpointDetails | Get endpoint details | epId | Query: include |
| PUT | `/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}` | updateARegisteredEndpoint | Update a registered endpoint | epId |
| PUT | `/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}/anc-policy` | applyANCPolicy | Apply ANC Policy | epId |
| DELETE | `/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}/anc-policy` | revokeANCPolicy | Revoke ANC policy | epId |
| POST | `/dna/intent/api/v1/endpoint-analytics/endpoints` | registerAnEndpoint | Register an endpoint |  |
| GET | `/dna/intent/api/v1/endpoint-analytics/endpoints` | queryTheEndpoints | Query the endpoints | Query: profilingStatus, macAddress, macAddresses, ip, deviceType, hardwareManufacturer, hardwareModel, operatingSystem, registered, randomMac, trustScore, authMethod, postureStatus, aiSpoofingTrustLevel, changedProfileTrustLevel, natTrustLevel, concurrentMacTrustLevel, ipBlocklistDetected, unauthPortDetected, weakCredDetected, ancPolicy, limit, offset, sortBy, order, include |
| POST | `/dna/intent/api/v1/endpoint-analytics/profiling-rules/bulk` | importProfilingRulesInBulk | Import profiling rules in bulk |  |
| POST | `/dna/intent/api/v1/endpoint-analytics/cmdb/endpoints` | processCMDBEndpoints | Process CMDB endpoints |  |
| GET | `/dna/intent/api/v1/endpoint-analytics/dictionaries` | getAIEndpointAnalyticsAttributeDictionaries | Get AI Endpoint Analytics attribute dictionaries | Query: includeAttributes |
| GET | `/dna/intent/api/v1/endpoint-analytics/anc-policies` | getANCPolicies | Get ANC policies |  |

#### Application Policy

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/applicationVisibility/networkDevices/enableAppTelemetry` | enableApplicationTelemetryFeatureOnMultipleNetworkDevices | Enable application telemetry feature on multiple network devices |  |
| DELETE | `/dna/intent/api/v1/app-policy-queuing-profile/{id}` | deleteApplicationPolicyQueuingProfile | Delete Application Policy Queuing Profile | id |
| GET | `/dna/intent/api/v2/application-policy-application-set` | getApplicationSet/s | Get Application Set/s | Query: attributes, name, offset, limit |
| POST | `/dna/intent/api/v2/application-policy-application-set` | createApplicationSet/s | Create Application Set/s |  |
| GET | `/dna/intent/api/v1/app-policy-queuing-profile` | getApplicationPolicyQueuingProfile | Get Application Policy Queuing Profile | Query: name |
| POST | `/dna/intent/api/v1/app-policy-queuing-profile` | createApplicationPolicyQueuingProfile | Create Application Policy Queuing Profile |  |
| PUT | `/dna/intent/api/v1/app-policy-queuing-profile` | updateApplicationPolicyQueuingProfile | Update Application Policy Queuing Profile |  |
| GET | `/dna/intent/api/v1/app-policy-default` | getApplicationPolicyDefault | Get Application Policy Default |  |
| GET | `/dna/intent/api/v1/qosPolicySetting` | retrievesTheApplicationQoSPolicySetting | Retrieves the application QoS policy setting |  |
| PUT | `/dna/intent/api/v1/qosPolicySetting` | updatesTheApplicationQoSPolicySetting | Updates the application QoS policy setting |  |
| POST | `/dna/intent/api/v1/qos-device-interface-info` | createQosDeviceInterfaceInfo | Create Qos Device Interface Info |  |
| GET | `/dna/intent/api/v1/qos-device-interface-info` | getQosDeviceInterfaceInfo | Get Qos Device Interface Info | Query: networkDeviceId |
| PUT | `/dna/intent/api/v1/qos-device-interface-info` | updateQosDeviceInterfaceInfo | Update Qos Device Interface Info |  |
| GET | `/dna/intent/api/v1/app-policy` | getApplicationPolicy | Get Application Policy | Query: policyScope |
| DELETE | `/dna/intent/api/v1/qos-device-interface-info/{id}` | deleteQosDeviceInterfaceInfo | Delete Qos Device Interface Info | id |
| GET | `/dna/intent/api/v1/applicationVisibility/networkDevices/count` | retrieveTheCountOfNetworkDevicesForTheGivenApplicationVisibilityStatusFilters | Retrieve the count of network devices for the given application visibility status filters | Query: ids, managementAddress, hostname, siteId, appTelemetryDeploymentStatus, appTelemetryReadinessStatus, cbarDeploymentStatus, cbarReadinessStatus, protocolPackStatus, protocolPackUpdateStatus, applicationRegistrySyncStatus |
| POST | `/dna/intent/api/v1/applicationVisibility/networkDevices/enableCbar` | enableCBARFeatureOnMultipleNetworkDevices | Enable CBAR feature on multiple network devices |  |
| PUT | `/dna/intent/api/v2/applications` | editApplication/s | Edit Application/s |  |
| GET | `/dna/intent/api/v2/applications` | getApplication/s | Get Application/s | Query: attributes, name, offset, limit |
| POST | `/dna/intent/api/v2/applications` | createApplication/s | Create Application/s |  |
| GET | `/dna/intent/api/v1/qos-device-interface-info-count` | getQosDeviceInterfaceInfoCount | Get Qos Device Interface Info Count |  |
| GET | `/dna/intent/api/v2/application-policy-application-set-count` | getApplicationSetCount | Get Application Set Count | Query: scalableGroupType |
| DELETE | `/dna/intent/api/v2/applications/{id}` | deleteApplication | Delete Application | id |
| POST | `/dna/intent/api/v1/applicationVisibility/networkDevices/disableCbar` | disableCBARFeatureOnMultipleNetworkDevices | Disable CBAR feature on multiple network devices |  |
| DELETE | `/dna/intent/api/v2/application-policy-application-set/{id}` | deleteApplicationSet | Delete Application Set | id |
| POST | `/dna/intent/api/v1/app-policy-intent` | applicationPolicyIntent | Application Policy Intent |  |
| GET | `/dna/intent/api/v2/applications-count` | getApplicationCount | Get Application Count | Query: scalableGroupType |
| GET | `/dna/intent/api/v1/applicationVisibility/networkDevices` | retrieveTheListOfNetworkDevicesWithTheirApplicationVisibilityStatus | Retrieve the list of network devices with their application visibility status | Query: ids, managementAddress, hostname, siteId, appTelemetryDeploymentStatus, appTelemetryReadinessStatus, cbarDeploymentStatus, cbarReadinessStatus, protocolPackStatus, protocolPackUpdateStatus, applicationRegistrySyncStatus, offset, limit, sortBy, order |
| GET | `/dna/intent/api/v1/app-policy-queuing-profile-count` | getApplicationPolicyQueuingProfileCount | Get Application Policy Queuing Profile Count |  |
| POST | `/dna/intent/api/v1/applicationVisibility/networkDevices/disableAppTelemetry` | disableApplicationTelemetryFeatureOnMultipleNetworkDevices | Disable application telemetry feature on multiple network devices |  |
| GET | `/dna/intent/api/v1/applications-count` | getApplicationsCount | Get Applications Count |  |
| PUT | `/dna/intent/api/v1/applications` | editApplication | Edit Application |  |
| DELETE | `/dna/intent/api/v1/applications` | deleteApplication-2 | Delete Application | Query: id |
| GET | `/dna/intent/api/v1/applications` | getApplications | Get Applications | Query: offset, limit, name |
| POST | `/dna/intent/api/v1/applications` | createApplication | Create Application |  |
| POST | `/dna/intent/api/v1/application-policy-application-set` | createApplicationSet | Create Application Set |  |
| DELETE | `/dna/intent/api/v1/application-policy-application-set` | deleteApplicationSet-2 | Delete Application Set | Query: id |
| GET | `/dna/intent/api/v1/application-policy-application-set` | getApplicationSets | Get Application Sets | Query: offset, limit, name |
| GET | `/dna/intent/api/v1/application-policy-application-set-count` | getApplicationSetsCount | Get Application Sets Count |  |

### Site Management

#### Configuration Archive

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/network-device-config` | getConfigurationArchiveDetails | Get configuration archive details | Query: deviceId, fileType, createdTime, createdBy, offset, limit |
| POST | `/dna/intent/api/v1/network-device-archive/cleartext` | exportDeviceConfigurations | Export Device configurations |  |
| POST | `/dna/intent/api/v1/networkDeviceConfigFiles/{id}/downloadUnmasked` | downloadUnmasked(raw)DeviceConfigurationAsZIP | Download Unmasked (raw) Device Configuration as ZIP | id |
| GET | `/dna/intent/api/v1/networkDeviceConfigFiles` | getNetworkDeviceConfigurationFileDetails | Get Network Device Configuration File Details | Query: id, networkDeviceId, fileType, offset, limit |
| GET | `/dna/intent/api/v1/networkDeviceConfigFiles/count` | countOfNetworkDeviceConfigurationFiles | Count of Network Device Configuration Files | Query: id, networkDeviceId, fileType |
| GET | `/dna/intent/api/v1/networkDeviceConfigFiles/{id}` | getConfigurationFileDetailsByID | Get Configuration File Details by ID | id |
| POST | `/dna/intent/api/v1/networkDeviceConfigFiles/{id}/downloadMasked` | downloadMaskedDeviceConfiguration | Download masked device configuration | id |

#### Configuration Templates

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/template-programmer/template/version/{templateId}` | getsAllTheVersionsOfAGivenTemplate | Gets all the versions of a given template | templateId |
| POST | `/dna/intent/api/v2/template-programmer/template/deploy` | deployTemplateV2 | Deploy Template V2 |  |
| POST | `/dna/intent/api/v1/template-programmer/clone/name/{name}/project/{projectId}/template/{templateId}` | createsACloneOfTheGivenTemplate | Creates a clone of the given template | name, templateId | Query: projectId |
| GET | `/dna/intent/api/v1/projects` | getTemplateProjects | Get Template Projects | Query: name, limit, offset |
| POST | `/dna/intent/api/v1/projects` | createTemplateProject | Create Template Project |  |
| POST | `/dna/intent/api/v1/template-programmer/template/deploy` | deployTemplate | Deploy Template |  |
| GET | `/dna/intent/api/v1/template-programmer/template/deploy/status/{deploymentId}` | statusOfTemplateDeployment | Status of template deployment | deploymentId |
| POST | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/bulk` | attachAListOfNetworkProfilesToADay-NCLITemplate | Attach a list of network profiles to a Day-N CLI template | templateId |
| DELETE | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/bulk` | detachAListOfNetworkProfilesFromADay-NCLITemplate | Detach a list of network profiles from a Day-N CLI template | templateId | Query: profileId |
| PUT | `/dna/intent/api/v1/template-programmer/template` | updateTemplate | Update Template |  |
| GET | `/dna/intent/api/v1/template-programmer/template` | getsTheTemplatesAvailable | Gets the templates available | Query: projectId, softwareType, softwareVersion, productFamily, productSeries, productType, filterConflictingTemplates, tags, projectNames, unCommitted, sortOrder |
| PUT | `/dna/intent/api/v1/template-programmer/template/preview` | previewTemplate | Preview Template |  |
| POST | `/dna/intent/api/v1/template-programmer/project/name/{projectName}/template/importtemplates` | importsTheTemplatesProvided | Imports the templates provided | projectName | Query: doVersion |
| GET | `/dna/intent/api/v1/template-programmer/project` | getsAListOfProjects | Gets a list of projects | Query: name, sortOrder |
| POST | `/dna/intent/api/v1/template-programmer/project` | createProject | Create Project |  |
| PUT | `/dna/intent/api/v1/template-programmer/project` | updateProject | Update Project |  |
| GET | `/dna/intent/api/v1/templates/{templateId}/versions/count` | getTemplateVersionsCount | Get Template Versions Count | templateId | Query: versionNumber, latestVersion |
| PUT | `/dna/intent/api/v1/projects/{projectId}` | updateTemplateProject | Update Template Project | projectId |
| GET | `/dna/intent/api/v1/projects/{projectId}` | getTemplateProject | Get Template Project | projectId |
| DELETE | `/dna/intent/api/v1/projects/{projectId}` | deleteTemplateProject | Delete Template Project | projectId |
| POST | `/dna/intent/api/v1/template-programmer/project/name/exportprojects` | exportsTheProjectsForAGivenCriteria. | Exports the projects for a given criteria. |  |
| GET | `/dna/intent/api/v1/templates/{templateId}/versions/{versionId}` | getTemplateVersion | Get Template Version | templateId, versionId |
| GET | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites` | retrieveTheNetworkProfilesAttachedToACLITemplate | Retrieve the network profiles attached to a CLI template | templateId |
| POST | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites` | attachNetworkProfileToADay-NCLITemplate | Attach network profile to a Day-N CLI template | templateId |
| DELETE | `/dna/intent/api/v1/template-programmer/project/{projectId}` | deletesTheProject | Deletes the project | projectId |
| GET | `/dna/intent/api/v1/template-programmer/project/{projectId}` | getsTheDetailsOfAGivenProject. | Gets the details of a given project. | projectId |
| GET | `/dna/intent/api/v1/template-programmer/template/{templateId}` | getsDetailsOfAGivenTemplate | Gets details of a given template | templateId | Query: latestVersion |
| DELETE | `/dna/intent/api/v1/template-programmer/template/{templateId}` | deletesTheTemplate | Deletes the template | templateId |
| GET | `/dna/intent/api/v2/template-programmer/project` | getProject(s)Details | Get project(s) details | Query: id, name, offset, limit, sortOrder |
| POST | `/dna/intent/api/v1/template-programmer/template/exporttemplates` | exportsTheTemplatesForAGivenCriteria. | Exports the templates for a given criteria. |  |
| GET | `/dna/intent/api/v1/templates/{templateId}/versions` | getTemplateVersions | Get Template Versions | templateId | Query: versionNumber, latestVersion, order, limit, offset |
| POST | `/dna/intent/api/v1/template-programmer/project/{projectId}/template` | createTemplate | Create Template | projectId |
| GET | `/dna/intent/api/v2/template-programmer/template` | getTemplate(s)Details | Get template(s) details | Query: id, name, projectId, projectName, softwareType, softwareVersion, productFamily, productSeries, productType, filterConflictingTemplates, tags, unCommitted, sortOrder, allTemplateAttributes, includeVersionDetails, offset, limit |
| DELETE | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/{profileId}` | detachANetworkProfileFromADay-NCLITemplate | Detach a network profile from a Day-N CLI template | templateId, profileId |
| POST | `/dna/intent/api/v1/templates/{templateId}/versions/commit` | commitTemplateForANewVersion | Commit Template For a New Version | templateId |
| GET | `/dna/intent/api/v1/projects/count` | getTemplateProjectCount | Get Template Project Count | Query: name |
| POST | `/dna/intent/api/v1/template-programmer/project/importprojects` | importsTheProjectsProvided | Imports the Projects provided | Query: doVersion |
| POST | `/dna/intent/api/v1/template-programmer/template/version` | versionTemplate | Version Template |  |
| GET | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/count` | retrieveCountOfNetworkProfilesAttachedToACLITemplate | Retrieve count of network profiles attached to a CLI template | templateId |

#### Device Onboarding (PnP)

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| PUT | `/dna/intent/api/v1/onboarding/pnp-device/{id}` | updateDevice | Update Device | id |
| GET | `/dna/intent/api/v1/onboarding/pnp-device/{id}` | getDeviceById | Get Device by Id | id |
| DELETE | `/dna/intent/api/v1/onboarding/pnp-device/{id}` | deleteDeviceByIdFromPnP | Delete Device by Id from PnP | id |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/unclaim` | un-ClaimDevice | Un-Claim Device |  |
| GET | `/dna/intent/api/v1/onboarding/pnp-device/sacct/{domain}/vacct/{name}/sync-result` | getSyncResultForVirtualAccount | Get Sync Result for Virtual Account | domain, name |
| POST | `/dna/intent/api/v1/onboarding/pnp-settings/savacct` | addVirtualAccount | Add Virtual Account |  |
| PUT | `/dna/intent/api/v1/onboarding/pnp-settings/savacct` | updatePnPServerProfile | Update PnP Server Profile |  |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/import` | importDevicesInBulk | Import Devices in bulk |  |
| DELETE | `/dna/intent/api/v1/onboarding/pnp-settings/vacct` | deregisterVirtualAccount | Deregister Virtual Account | Query: domain, name |
| POST | `/api/v1/onboarding/pnp-device/authorize` | authorizeDevice | Authorize Device |  |
| PUT | `/dna/intent/api/v1/onboarding/pnp-workflow/{id}` | updateWorkflow | Update Workflow | id |
| GET | `/dna/intent/api/v1/onboarding/pnp-workflow/{id}` | getWorkflowById | Get Workflow by Id | id |
| DELETE | `/dna/intent/api/v1/onboarding/pnp-workflow/{id}` | deleteWorkflowById | Delete Workflow By Id | id |
| GET | `/dna/intent/api/v1/onboarding/pnp-settings/sacct` | getSmartAccountList | Get Smart Account List |  |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/site-claim` | claimADeviceToASite | Claim a Device to a Site |  |
| GET | `/dna/intent/api/v1/onboarding/pnp-settings/sacct/{domain}/vacct` | getVirtualAccountList | Get Virtual Account List | domain |
| GET | `/dna/intent/api/v1/onboarding/pnp-workflow/count` | getWorkflowCount | Get Workflow Count | Query: name |
| GET | `/dna/intent/api/v1/onboarding/pnp-settings` | getPnPGlobalSettings | Get PnP global settings |  |
| PUT | `/dna/intent/api/v1/onboarding/pnp-settings` | updatePnPGlobalSettings | Update PnP global settings |  |
| POST | `/dna/intent/api/v1/onboarding/pnp-workflow` | addAWorkflow | Add a Workflow |  |
| GET | `/dna/intent/api/v1/onboarding/pnp-workflow` | getWorkflows | Get Workflows | Query: limit, offset, sort, sortOrder, type, name |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/vacct-sync` | syncVirtualAccountDevices | Sync Virtual Account Devices |  |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/reset` | resetDevice | Reset Device |  |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/claim` | claimDevice | Claim Device |  |
| POST | `/dna/intent/api/v1/onboarding/pnp-device/site-config-preview` | previewConfig | Preview Config |  |
| GET | `/dna/intent/api/v1/onboarding/pnp-device/count` | getDeviceCount-2 | Get Device Count | Query: serialNumber, state, onbState, name, pid, source, workflowId, workflowName, smartAccountId, virtualAccountId, lastContact |
| GET | `/dna/intent/api/v1/onboarding/pnp-device/history` | getDeviceHistory | Get Device History | Query: serialNumber, sort, sortOrder |
| GET | `/dna/intent/api/v1/onboarding/pnp-device` | getDeviceList-2 | Get Device list | Query: limit, offset, sort, sortOrder, serialNumber, state, onbState, name, pid, source, workflowId, workflowName, smartAccountId, virtualAccountId, lastContact, macAddress, hostname, siteName |
| POST | `/dna/intent/api/v1/onboarding/pnp-device` | addDevice-2 | Add Device |  |

#### Device Replacement

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/device-replacement/workflow` | deployDeviceReplacementWorkflow | Deploy device replacement workflow |  |
| PUT | `/dna/intent/api/v1/device-replacement` | unMarkDeviceForReplacement | UnMark device for replacement |  |
| POST | `/dna/intent/api/v1/device-replacement` | markDeviceForReplacement | Mark device for replacement |  |
| GET | `/dna/intent/api/v1/device-replacement` | returnListOfReplacementDevicesWithReplacementDetails | Return list of replacement devices with replacement details | Query: faultyDeviceName, faultyDevicePlatform, replacementDevicePlatform, faultyDeviceSerialNumber, replacementDeviceSerialNumber, replacementStatus, family, sortBy, sortOrder, offset, limit |
| GET | `/dna/intent/api/v1/networkDeviceReplacements/{id}` | retrieveTheStatusOfDeviceReplacementWorkflowThatReplacesAFaultyDeviceWithAReplacementDevice. | Retrieve the status of device replacement workflow that replaces a faulty device with a replacement device. | id |
| GET | `/dna/intent/api/v1/device-replacement/count` | returnReplacementDevicesCount | Return replacement devices count | Query: replacementStatus |
| GET | `/dna/intent/api/v1/networkDeviceReplacements` | retrieveTheStatusOfAllTheDeviceReplacementWorkflows. | Retrieve the status of all the device replacement workflows. | Query: family, faultyDeviceName, faultyDevicePlatform, faultyDeviceSerialNumber, replacementDevicePlatform, replacementDeviceSerialNumber, replacementStatus, offset, limit, sortBy, sortOrder |

#### LAN Automation

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/lanAutomation/portChannels/{id}/removeLink` | removeALinkFromPortChannel | Remove a link from Port Channel | id |
| PUT | `/dna/intent/api/v1/lan-automation/{id}` | lANAutomationStopAndUpdateDevices | LAN Automation Stop and Update Devices | id |
| DELETE | `/dna/intent/api/v1/lan-automation/{id}` | lANAutomationStop | LAN Automation Stop | id |
| PUT | `/dna/intent/api/v1/lan-automation/updateDevice` | lANAutomationDeviceUpdate | LAN Automation Device Update | Query: feature |
| GET | `/dna/intent/api/v1/lanAutomation/portChannels/{id}` | getPortChannelInformationById | Get Port Channel information by id | id |
| DELETE | `/dna/intent/api/v1/lanAutomation/portChannels/{id}` | deletePortChannel | Delete Port Channel | id |
| POST | `/dna/intent/api/v1/lanAutomation/portChannels` | createANewPortChannelBetweenDevices | Create a New Port Channel between devices |  |
| GET | `/dna/intent/api/v1/lanAutomation/portChannels` | getPortChannels | Get Port Channels | Query: device1ManagementIPAddress, device1Uuid, device2ManagementIPAddress, device2Uuid, offset, limit |
| GET | `/dna/intent/api/v1/lan-automation/log/{id}` | lANAutomationLogById | LAN Automation Log by Id | id |
| GET | `/dna/intent/api/v1/lan-automation/status/{id}` | lANAutomationStatusById | LAN Automation Status by Id | id |
| POST | `/dna/intent/api/v2/lan-automation` | lANAutomationStartV2 | LAN Automation Start V2 |  |
| GET | `/dna/intent/api/v1/lan-automation/log` | lANAutomationLog | LAN Automation Log  | Query: offset, limit |
| PUT | `/dna/intent/api/v2/lan-automation/{id}` | lANAutomationStopAndUpdateDevicesV2 | LAN Automation Stop and Update Devices V2 | id |
| POST | `/dna/intent/api/v1/lan-automation` | lANAutomationStart | LAN Automation Start |  |
| GET | `/dna/intent/api/v1/lan-automation/status` | lANAutomationStatus | LAN Automation Status | Query: offset, limit |
| GET | `/dna/intent/api/v1/lan-automation/log/{id}/{serialNumber}` | lANAutomationLogsForIndividualDevices | LAN Automation Logs for Individual Devices | id, serialNumber | Query: logLevel |
| GET | `/dna/intent/api/v1/lan-automation/count` | lANAutomationSessionCount | LAN Automation Session Count |  |
| GET | `/dna/intent/api/v1/lan-automation/sessions` | lANAutomationActiveSessions | LAN Automation Active Sessions |  |
| POST | `/dna/intent/api/v1/lanAutomation/portChannels/{id}/addLink` | addALANAutomatedLinkToAPortChannel | Add a LAN Automated link to a Port Channel | id |

#### Network Settings

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/ipam/siteIpAddressPools/count` | countsIPAddressSubpools. | Counts IP address subpools. | Query: siteId |
| GET | `/dna/intent/api/v1/sites/{id}/telemetrySettings` | retrieveTelemetrySettingsForASite | Retrieve Telemetry settings for a site | id | Query: _inherited |
| PUT | `/dna/intent/api/v1/sites/{id}/telemetrySettings` | setTelemetrySettingsForASite | Set Telemetry settings for a site | id |
| PUT | `/dna/intent/api/v1/sites/{id}/bannerSettings` | setBannerSettingsForASite | Set banner settings for a site | id |
| GET | `/dna/intent/api/v1/sites/{id}/bannerSettings` | retrieveBannerSettingsForASite | Retrieve banner settings for a site | id | Query: _inherited |
| POST | `/dna/intent/api/v2/credential-to-site/{siteId}` | assignDeviceCredentialToSiteV2 | Assign Device Credential To Site V2 | siteId |
| GET | `/dna/intent/api/v1/sites/{id}/deviceCredentials/status` | getNetworkDevicesCredentialsSyncStatus | Get network devices credentials sync status | id |
| POST | `/dna/intent/api/v1/telemetrySettings/apply` | updateADevice(s)TelemetrySettingsToConformToTheTelemetrySettingsForItsSite | Update a device(s) telemetry settings to conform to the telemetry settings for its site |  |
| PUT | `/dna/intent/api/v1/sites/{id}/timeZoneSettings` | setTimeZoneForASite | Set time zone for a site | id |
| GET | `/dna/intent/api/v1/sites/{id}/timeZoneSettings` | retrieveTimeZoneSettingsForASite | Retrieve time zone settings for a site | id | Query: _inherited |
| PUT | `/dna/intent/api/v1/sites/{id}/aaaSettings` | setAAASettingsForASite | Set AAA settings for a site | id |
| GET | `/dna/intent/api/v1/sites/{id}/aaaSettings` | retrieveAAASettingsForASite | Retrieve AAA settings for a site | id | Query: _inherited |
| GET | `/dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAddressPoolId}/subpools/count` | countsSubpoolsOfAGlobalIPAddressPool. | Counts subpools of a global IP address pool. | globalIpAddressPoolId |
| POST | `/dna/intent/api/v2/network/{siteId}` | createNetworkV2 | Create Network V2 | siteId |
| PUT | `/dna/intent/api/v2/network/{siteId}` | updateNetworkV2 | Update Network V2 | siteId |
| DELETE | `/dna/intent/api/v2/sp-profile/{spProfileName}` | deleteSPProfileV2 | Delete SP Profile V2 | spProfileName |
| POST | `/dna/intent/api/v1/sites/deviceCredentials/apply` | syncNetworkDevicesCredential | Sync network devices credential |  |
| GET | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/templates/count` | retrieveCountOfCLITemplatesAttachedToANetworkProfile | Retrieve count of CLI templates attached to a network profile | profileId |
| PUT | `/dna/intent/api/v1/sites/{id}/deviceCredentials` | updateDeviceCredentialSettingsForASite. | Update device credential settings for a site. | id |
| GET | `/dna/intent/api/v1/sites/{id}/deviceCredentials` | getDeviceCredentialSettingsForASite | Get device credential settings for a site | id | Query: _inherited |
| PUT | `/dna/intent/api/v1/ipam/globalIpAddressPools/{id}` | updatesAGlobalIPAddressPool. | Updates a global IP address pool. | id |
| GET | `/dna/intent/api/v1/ipam/globalIpAddressPools/{id}` | retrievesAGlobalIPAddressPool. | Retrieves a global IP address pool. | id |
| DELETE | `/dna/intent/api/v1/ipam/globalIpAddressPools/{id}` | deleteAGlobalIPAddressPool. | Delete a global IP address pool. | id |
| GET | `/dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAddressPoolId}/subpools` | retrievesSubpoolsIDsOfAGlobalIPAddressPool. | Retrieves subpools IDs of a global IP address pool. | globalIpAddressPoolId | Query: offset, limit |
| GET | `/dna/intent/api/v1/ipam/globalIpAddressPools` | retrievesGlobalIPAddressPools. | Retrieves global IP address pools. | Query: offset, limit, sortBy, order |
| POST | `/dna/intent/api/v1/ipam/globalIpAddressPools` | createAGlobalIPAddressPool. | Create a global IP address pool. |  |
| PUT | `/dna/intent/api/v2/service-provider` | updateSPProfileV2 | Update SP Profile V2 |  |
| POST | `/dna/intent/api/v2/service-provider` | createSPProfileV2 | Create SP Profile V2 |  |
| GET | `/dna/intent/api/v2/service-provider` | getServiceProviderDetailsV2 | Get Service Provider Details V2 |  |
| PUT | `/dna/intent/api/v1/sites/{id}/dnsSettings` | setDNSSettingsForASite | Set DNS settings for a site | id |
| GET | `/dna/intent/api/v1/sites/{id}/dnsSettings` | retrieveDNSSettingsForASite | Retrieve DNS settings for a site | id | Query: _inherited |
| PUT | `/dna/intent/api/v1/sites/{id}/imageDistributionSettings` | setImageDistributionSettingsForASite | Set image distribution settings for a site | id |
| GET | `/dna/intent/api/v1/sites/{id}/imageDistributionSettings` | retrieveImageDistributionSettingsForASite | Retrieve image distribution settings for a site | id | Query: _inherited |
| GET | `/dna/intent/api/v1/ipam/siteIpAddressPools/{id}` | retrievesAnIPAddressSubpool. | Retrieves an IP address subpool. | id |
| PUT | `/dna/intent/api/v1/ipam/siteIpAddressPools/{id}` | updatesAnIPAddressSubpool. | Updates an IP address subpool. | id |
| DELETE | `/dna/intent/api/v1/ipam/siteIpAddressPools/{id}` | releaseAnIPAddressSubpool. | Release an IP address subpool. | id |
| PUT | `/dna/intent/api/v1/sites/{id}/ntpSettings` | setNTPSettingsForASite | Set NTP settings for a site | id |
| GET | `/dna/intent/api/v1/sites/{id}/ntpSettings` | retrieveNTPSettingsForASite | Retrieve NTP settings for a site | id | Query: _inherited |
| GET | `/dna/intent/api/v1/ipam/siteIpAddressPools` | retrievesIPAddressSubpools. | Retrieves IP address subpools. | Query: offset, limit, sortBy, order, siteId |
| POST | `/dna/intent/api/v1/ipam/siteIpAddressPools` | reserve(create)IPAddressSubpools. | Reserve (create) IP address subpools. |  |
| GET | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/templates` | retrieveCLITemplatesAttachedToANetworkProfile | Retrieve CLI templates attached to a network profile | profileId |
| GET | `/dna/intent/api/v1/sites/{id}/dhcpSettings` | retrieveDHCPSettingsForASite | Retrieve DHCP settings for a site | id | Query: _inherited |
| PUT | `/dna/intent/api/v1/sites/{id}/dhcpSettings` | setDhcpSettingsForASite | Set dhcp settings for a site | id |
| GET | `/dna/intent/api/v1/ipam/globalIpAddressPools/count` | countsGlobalIPAddressPools. | Counts global IP address pools. |  |
| GET | `/dna/intent/api/v2/network` | getNetworkV2 | Get Network V2 | Query: siteId |
| DELETE | `/dna/intent/api/v1/global-pool/{id}` | deleteGlobalIPPool | Delete Global IP Pool | id |
| GET | `/dna/intent/api/v1/network` | getNetwork | Get Network | Query: siteId |
| DELETE | `/dna/intent/api/v1/sp-profile/{spProfileName}` | deleteSPProfile | Delete SP Profile | spProfileName |
| GET | `/dna/intent/api/v1/reserve-ip-subpool` | getReserveIPSubpool | Get Reserve IP Subpool | Query: siteId, offset, limit, ignoreInheritedGroups, poolUsage, groupName |
| GET | `/dna/intent/api/v1/service-provider` | getServiceProviderDetails | Get Service provider Details |  |
| PUT | `/dna/intent/api/v1/service-provider` | updateSPProfile | Update SP Profile |  |
| POST | `/dna/intent/api/v1/service-provider` | createSPProfile | Create SP Profile |  |
| PUT | `/dna/intent/api/v1/network/{siteId}` | updateNetwork | Update Network | siteId |
| POST | `/dna/intent/api/v1/network/{siteId}` | createNetwork | Create Network | siteId |
| PUT | `/dna/intent/api/v1/global-pool` | updateGlobalPool | Update Global Pool |  |
| GET | `/dna/intent/api/v1/global-pool` | getGlobalPool | Get Global Pool | Query: offset, limit |
| POST | `/dna/intent/api/v1/global-pool` | createGlobalPool | Create Global Pool |  |
| GET | `/dna/intent/api/v1/device-credential` | getDeviceCredentialDetails | Get Device Credential Details | Query: siteId |
| PUT | `/dna/intent/api/v1/device-credential` | updateDeviceCredentials | Update Device Credentials |  |
| POST | `/dna/intent/api/v1/device-credential` | createDeviceCredentials | Create Device Credentials |  |
| POST | `/dna/intent/api/v1/reserve-ip-subpool/{siteId}` | reserveIPSubpool | Reserve IP Subpool | siteId |
| PUT | `/dna/intent/api/v1/reserve-ip-subpool/{siteId}` | updateReserveIPSubpool | Update Reserve IP Subpool | siteId | Query: id |
| DELETE | `/dna/intent/api/v1/device-credential/{id}` | deleteDeviceCredential | Delete Device Credential | id |
| POST | `/dna/intent/api/v1/credential-to-site/{siteId}` | assignDeviceCredentialToSite | Assign Device Credential To Site | siteId |
| DELETE | `/dna/intent/api/v1/reserve-ip-subpool/{id}` | releaseReserveIPSubpool | Release Reserve IP Subpool | id |

#### Site Design

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| PUT | `/dna/intent/api/v2/buildings/{id}` | updatesABuilding | Updates a building | id |
| DELETE | `/dna/intent/api/v2/buildings/{id}` | deletesABuilding | Deletes a building | id |
| GET | `/dna/intent/api/v2/buildings/{id}` | getsABuilding | Gets a building | id |
| GET | `/dna/intent/api/v1/networkDevices/deviceControllability/settings` | getDeviceControllabilitySettings | Get device controllability settings |  |
| PUT | `/dna/intent/api/v1/networkDevices/deviceControllability/settings` | updateDeviceControllabilitySettings | Update device controllability settings |  |
| POST | `/dna/intent/api/v1/networkDevices/unassignFromSite/apply` | unassignNetworkDevicesFromSites | Unassign network devices from sites |  |
| GET | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments` | retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo | Retrieves the list of sites that the given network profile for sites is assigned to | profileId | Query: offset, limit |
| POST | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments` | assignANetworkProfileForSitesToTheGivenSite | Assign a network profile for sites to the given site | profileId |
| GET | `/dna/intent/api/v1/sites/count` | getSitesCount | Get sites count | Query: name |
| PUT | `/dna/intent/api/v2/floors/settings` | updatesFloorSettings | Updates floor settings |  |
| GET | `/dna/intent/api/v2/floors/settings` | getFloorSettings | Get floor settings |  |
| POST | `/dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions/assignAccessPointPositions` | assignPlannedAccessPointsToOperationsOnes | Assign Planned Access Points to operations ones | floorId |
| POST | `/dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions/bulkChange` | editPlannedAccessPointsPositions | Edit Planned Access Points Positions | floorId |
| GET | `/dna/intent/api/v1/networkDevices/assignedToSite` | getSiteAssignedNetworkDevices | Get site assigned network devices | Query: siteId, offset, limit |
| GET | `/dna/intent/api/v1/sites/{siteId}/profileAssignments/count` | retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned | Retrieves the count of profiles that the given site has been assigned | siteId |
| DELETE | `/dna/intent/api/v1/areas/{id}` | deletesAnArea | Deletes an area | id |
| GET | `/dna/intent/api/v1/areas/{id}` | getsAnArea | Gets an area | id |
| PUT | `/dna/intent/api/v1/areas/{id}` | updatesAnArea | Updates an area | id |
| POST | `/dna/intent/api/v1/networkprofile/{networkProfileId}/site/{siteId}` | associate | Associate | networkProfileId, siteId |
| DELETE | `/dna/intent/api/v1/networkprofile/{networkProfileId}/site/{siteId}` | disassociate | Disassociate | networkProfileId, siteId |
| GET | `/dna/intent/api/v1/sites` | getSites | Get sites | Query: name, nameHierarchy, type, _unitsOfMeasure, offset, limit |
| GET | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/count` | retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo | Retrieves the count of sites that the given network profile for sites is assigned to | profileId |
| GET | `/dna/intent/api/v1/networkProfilesForSites/count` | retrievesTheCountOfNetworkProfilesForSites | Retrieves the count of network profiles for sites | Query: type |
| GET | `/dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions/count` | getPlannedAccessPointsPositionsCount | Get Planned Access Points Positions count | floorId | Query: name, macAddress, type |
| DELETE | `/dna/intent/api/v2/floors/{id}` | deletesAFloor | Deletes a floor | id |
| PUT | `/dna/intent/api/v2/floors/{id}` | updatesAFloor | Updates a floor | id |
| GET | `/dna/intent/api/v2/floors/{id}` | getsAFloor | Gets a floor | id | Query: _unitsOfMeasure |
| POST | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/bulk` | assignANetworkProfileForSitesToAListOfSites | Assign a network profile for sites to a list of sites | profileId |
| DELETE | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/bulk` | unassignsANetworkProfileForSitesFromMultipleSites | Unassigns a network profile for sites from multiple sites | profileId | Query: siteId |
| GET | `/dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions` | getPlannedAccessPointsPositions | Get Planned Access Points Positions | floorId | Query: name, macAddress, type, offset, limit |
| POST | `/dna/intent/api/v2/buildings` | createsABuilding | Creates a building |  |
| GET | `/dna/intent/api/v1/networkProfilesForSites/{id}` | retrieveANetworkProfileForSitesById | Retrieve a network profile for sites by id | id |
| DELETE | `/dna/intent/api/v1/networkProfilesForSites/{id}` | deletesANetworkProfileForSites | Deletes a network profile for sites | id |
| POST | `/dna/intent/api/v2/floors` | createsAFloor | Creates a floor |  |
| DELETE | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/{id}` | unassignsANetworkProfileForSitesFromASite | Unassigns a network profile for sites from a site | profileId, id |
| POST | `/dna/intent/api/v1/networkDevices/assignToSite/apply` | assignNetworkDevicesToASite | Assign network devices to a site |  |
| GET | `/dna/intent/api/v1/networkProfilesForSites` | retrievesTheListOfNetworkProfilesForSites | Retrieves the list of network profiles for sites | Query: offset, limit, sortBy, order, type |
| GET | `/dna/intent/api/v1/sites/{siteId}/profileAssignments` | retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned | Retrieves the list of network profiles that the given site has been assigned | siteId | Query: offset, limit |
| POST | `/dna/intent/api/v1/areas` | createsAnArea | Creates an area |  |
| POST | `/dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions/bulk` | addPlannedAccessPointsPositions | Add Planned Access Points Positions | floorId |
| GET | `/dna/intent/api/v1/networkDevices/notAssignedToSite/count` | getSiteNotAssignedNetworkDevicesCount | Get site not assigned network devices count |  |
| GET | `/dna/intent/api/v1/networkDevices/notAssignedToSite` | getSiteNotAssignedNetworkDevices | Get site not assigned network devices | Query: offset, limit |
| POST | `/dna/intent/api/v2/floors/{floorId}/accessPointPositions/bulkChange` | editTheAccessPointsPositions | Edit the Access Points Positions | floorId |
| GET | `/dna/intent/api/v2/floors/{floorId}/accessPointPositions/count` | getAccessPointsPositionsCount | Get Access Points positions count | floorId | Query: name, macAddress, type, model |
| GET | `/dna/intent/api/v1/networkDevices/{id}/assignedToSite` | getSiteAssignedNetworkDevice | Get site assigned network device | id |
| DELETE | `/dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions/{id}` | deletePlannedAccessPointsPosition | Delete Planned Access Points Position | floorId, id |
| GET | `/dna/intent/api/v1/networkDevices/assignedToSite/count` | getSiteAssignedNetworkDevicesCount | Get site assigned network devices count | Query: siteId |
| POST | `/dna/intent/api/v1/sites/bulk` | createSites | Create sites |  |
| GET | `/dna/intent/api/v2/floors/{floorId}/accessPointPositions` | getAccessPointsPositions | Get Access Points positions | floorId | Query: name, macAddress, type, model, offset, limit |
| POST | `/dna/intent/api/v2/floors/{id}/uploadImage` | uploadsFloorImage | Uploads floor image | id |

#### Software Image Management (SWIM)

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` | assignNetworkDeviceProductNameToTheGivenSoftwareImage | Assign network device product name to the given software image | imageId |
| GET | `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` | retrievesNetworkDeviceProductNamesAssignedToASoftwareImage. | Retrieves network device product names assigned to a software image. | imageId | Query: productName, productId, recommended, assigned, offset, limit |
| GET | `/dna/intent/api/v1/siteWiseProductNames/count` | returnsTheCountOfNetworkDeviceProductNamesForASite | Returns the count of network device product names for a site | Query: siteId, productName |
| DELETE | `/dna/intent/api/v1/images/{id}` | deleteImage | Delete image | id |
| GET | `/dna/intent/api/v1/image/importation` | getSoftwareImageDetails | Get software image details | Query: imageUuid, name, family, applicationType, imageIntegrityStatus, version, imageSeries, imageName, isTaggedGolden, isCCORecommended, isCCOLatest, createdTime, imageSizeGreaterThan, imageSizeLesserThan, sortBy, sortOrder, limit, offset |
| GET | `/dna/intent/api/v1/images/count` | returnsCountOfSoftwareImages | Returns count of software images | Query: siteId, productNameOrdinal, supervisorProductNameOrdinal, imported, name, version, golden, integrity, hasAddonImages, isAddonImages |
| POST | `/dna/intent/api/v1/image/importation/source/file` | importLocalSoftwareImage | Import local software image | Query: isThirdParty, thirdPartyVendor, thirdPartyImageFamily, thirdPartyApplicationType |
| POST | `/dna/intent/api/v1/images/distributionServerSettings` | addImageDistributionServer | Add image distribution server |  |
| GET | `/dna/intent/api/v1/images/distributionServerSettings` | retrieveImageDistributionServers | Retrieve image distribution servers |  |
| PUT | `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames/{productNameOrdinal}` | updateTheListOfSitesForTheNetworkDeviceProductNameAssignedToTheSoftwareImage | Update the list of sites for the network device product name assigned to the software image | imageId, productNameOrdinal |
| DELETE | `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames/{productNameOrdinal}` | unassignNetworkDeviceProductNameFromTheGivenSoftwareImage | Unassign network device product name from the given software image | imageId, productNameOrdinal |
| GET | `/dna/intent/api/v1/siteWiseProductNames` | returnsNetworkDeviceProductNamesForASite | Returns network device product names for a site | Query: siteId, productName, offset, limit |
| POST | `/dna/intent/api/v1/images/{id}/sites/{siteId}/tagGolden` | taggingGoldenImage | Tagging golden image | id, siteId |
| POST | `/dna/intent/api/v1/images/ccoSync` | initiatesSyncOfSoftwareImagesFromCisco.com | Initiates sync of software images from Cisco.com |  |
| PUT | `/dna/intent/api/v1/images/distributionServerSettings/{id}` | updateRemoteImageDistributionServer | Update remote image distribution server | id |
| DELETE | `/dna/intent/api/v1/images/distributionServerSettings/{id}` | removeImageDistributionServer | Remove image distribution server | id |
| GET | `/dna/intent/api/v1/images/distributionServerSettings/{id}` | retrieveSpecificImageDistributionServer | Retrieve specific image distribution server | id |
| GET | `/dna/intent/api/v1/image/importation/device-family-identifiers` | getDeviceFamilyIdentifiers | Get Device Family Identifiers |  |
| GET | `/dna/intent/api/v1/productNames/{productNameOrdinal}` | retrieveNetworkDeviceProductName | Retrieve network device product name | productNameOrdinal |
| POST | `/dna/intent/api/v1/image/importation/golden` | tagAsGoldenImage | Tag as Golden Image |  |
| GET | `/dna/intent/api/v1/siteWiseImagesSummary` | returnsTheImageSummaryForTheGivenSite | Returns the image summary for the given site | Query: siteId |
| GET | `/dna/intent/api/v1/networkDeviceImageUpdates` | getNetworkDeviceImageUpdates | Get network device image updates | Query: id, parentId, networkDeviceId, status, imageName, hostName, managementAddress, startTime, endTime, sortBy, order, offset, limit |
| POST | `/dna/intent/api/v1/images/{id}/sites/{siteId}/untagGolden` | untaggingGoldenImage | Untagging golden image | id, siteId |
| POST | `/dna/intent/api/v1/image/distribution` | triggerSoftwareImageDistribution | Trigger software image distribution |  |
| GET | `/dna/intent/api/v1/image/importation/golden/site/{siteId}/family/{deviceFamilyIdentifier}/role/{deviceRole}/image/{imageId}` | getGoldenTagStatusOfAnImage. | Get Golden Tag Status of an Image. | siteId, deviceFamilyIdentifier, deviceRole, imageId |
| DELETE | `/dna/intent/api/v1/image/importation/golden/site/{siteId}/family/{deviceFamilyIdentifier}/role/{deviceRole}/image/{imageId}` | removeGoldenTagForImage. | Remove Golden Tag for image. | siteId, deviceFamilyIdentifier, deviceRole, imageId |
| GET | `/dna/intent/api/v1/productNames` | retrievesTheListOfNetworkDeviceProductNames | Retrieves the list of network device product names | Query: productName, productId, offset, limit |
| GET | `/dna/intent/api/v1/productNames/count` | countOfNetworkProductNames | Count of network product names | Query: productName, productId |
| GET | `/dna/intent/api/v1/networkDeviceImageUpdates/count` | countOfNetworkDeviceImageUpdates | Count of network device image updates | Query: id, parentId, networkDeviceId, status, imageName, hostName, managementAddress, startTime, endTime |
| POST | `/dna/intent/api/v1/image/importation/source/url` | importSoftwareImageViaURL | Import software image via URL | Query: scheduleAt, scheduleDesc, scheduleOrigin |
| POST | `/dna/intent/api/v1/images/{id}/download` | downloadTheSoftwareImage | Download the software image | id |
| GET | `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames/count` | retrievesTheCountOfAssignedNetworkDeviceProducts | Retrieves the count of assigned network device products | imageId | Query: productName, productId, recommended, assigned |
| GET | `/dna/intent/api/v1/images` | returnsListOfSoftwareImages | Returns list of software images | Query: siteId, productNameOrdinal, supervisorProductNameOrdinal, imported, name, version, golden, integrity, hasAddonImages, isAddonImages, offset, limit |
| GET | `/dna/intent/api/v1/images/{id}/addonImages/count` | returnsCountOfAdd-onImages | Returns count of add-on images | id |
| GET | `/dna/intent/api/v1/images/{id}/addonImages` | retrieveApplicableAdd-onImagesForTheGivenSoftwareImage | Retrieve applicable add-on images for the given software image | id |
| POST | `/dna/intent/api/v1/image/activation/device` | triggerSoftwareImageActivation | Trigger software image activation | Query: scheduleValidate |

### System

#### Cisco Trusted Certificates

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| POST | `/dna/intent/api/v1/trustedCertificates/import` | importTrustedCertificate | Import Trusted Certificate |  |

#### Health and Performance

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/diagnosticTasks/{id}` | retrievesDiagnosticTaskByID | Retrieves diagnostic task by ID | id |
| GET | `/dna/intent/api/v1/diagnosticTasks/{id}/detail` | retrievesDiagnosticTaskDetailsByID | Retrieves diagnostic task details by ID | id |

#### Licenses

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/intent/api/v1/networkDeviceLicenses/summary` | retrievesSummaryOfNetworkDeviceLicenses | Retrieves summary of network device licenses |  |

#### User and Roles

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| GET | `/dna/system/api/v1/users/external-servers/aaa-attribute` | getAAAAttributeAPI | Get AAA Attribute API |  |
| POST | `/dna/system/api/v1/users/external-servers/aaa-attribute` | addAndUpdateAAAAttributeAPI | Add and Update AAA Attribute API |  |
| DELETE | `/dna/system/api/v1/users/external-servers/aaa-attribute` | deleteAAAAttributeAPI | Delete AAA Attribute API |  |
| PUT | `/dna/system/api/v1/role` | updateRoleAPI | Update role API |  |
| POST | `/dna/system/api/v1/role` | addRoleAPI | Add role API |  |
| DELETE | `/dna/system/api/v1/user/{userId}` | deleteUserAPI | Delete user API | userId |
| POST | `/dna/system/api/v1/user` | addUserAPI | Add user API |  |
| GET | `/dna/system/api/v1/user` | getUsersAPI | Get users API | Query: invokeSource, authSource |
| PUT | `/dna/system/api/v1/user` | updateUserAPI | Update user API |  |
| GET | `/dna/system/api/v1/roles` | getRolesAPI | Get roles API |  |
| GET | `/dna/system/api/v1/role/permissions` | getPermissionsAPI | Get permissions API |  |
| GET | `/dna/system/api/v1/users/external-servers` | getExternalAuthenticationServersAPI | Get external authentication servers API | Query: invokeSource |
| GET | `/dna/system/api/v1/users/external-authentication` | getExternalAuthenticationSettingAPI | Get External Authentication Setting API |  |
| POST | `/dna/system/api/v1/users/external-authentication` | manageExternalAuthenticationSettingAPI | Manage External Authentication Setting API |  |
| DELETE | `/dna/system/api/v1/role/{roleId}` | deleteRoleAPI | Delete role API | roleId |

### System Settings

#### 

| Method | Path | Operation ID | Summary | Parameters |
|--------|------|-------------|---------|------------|
| DELETE | `/dna/intent/api/v1/authentication-policy-servers/{id}` | deleteAuthenticationAndPolicyServerAccessConfiguration | Delete Authentication and Policy Server Access Configuration | id |
| PUT | `/dna/intent/api/v1/authentication-policy-servers/{id}` | editAuthenticationAndPolicyServerAccessConfiguration | Edit Authentication and Policy Server Access Configuration | id |
| GET | `/dna/intent/api/v1/network-device/custom-prompt` | custom-promptSupportGETAPI | Custom-prompt support GET API |  |
| POST | `/dna/intent/api/v1/network-device/custom-prompt` | customPromptPOSTAPI | Custom Prompt POST API |  |
| POST | `/dna/intent/api/v1/ipam/serverSetting` | createsConfigurationDetailsOfTheExternalIPAMServer. | Creates configuration details of the external IPAM server. |  |
| GET | `/dna/intent/api/v1/ipam/serverSetting` | retrievesConfigurationDetailsOfTheExternalIPAMServer. | Retrieves configuration details of the external IPAM server. |  |
| PUT | `/dna/intent/api/v1/ipam/serverSetting` | updatesConfigurationDetailsOfTheExternalIPAMServer. | Updates configuration details of the external IPAM server. |  |
| DELETE | `/dna/intent/api/v1/ipam/serverSetting` | deletesConfigurationDetailsOfTheExternalIPAMServer. | Deletes configuration details of the external IPAM server. |  |
| POST | `/dna/intent/api/v1/authentication-policy-servers` | addAuthenticationAndPolicyServerAccessConfiguration | Add Authentication and Policy Server Access Configuration |  |
| GET | `/dna/intent/api/v1/authentication-policy-servers` | getAuthenticationAndPolicyServers | Get Authentication and Policy Servers | Query: isIseEnabled, state, role |
| GET | `/dna/intent/api/v1/provisioningSettings` | getProvisioningSettings | Get provisioning settings |  |
| PUT | `/dna/intent/api/v1/provisioningSettings` | setProvisioningSettings | Set provisioning settings |  |
| PUT | `/dna/intent/api/v1/integrate-ise/{id}` | acceptCiscoISEServerCertificateForCiscoISEServerIntegration | Accept Cisco ISE Server Certificate for Cisco ISE Server Integration | id |
| GET | `/dna/intent/api/v1/ise-integration-status` | ciscoISEServerIntegrationStatus | Cisco ISE Server Integration Status |  |

