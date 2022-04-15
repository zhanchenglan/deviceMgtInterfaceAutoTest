"""
Copyright @2022-01-17 Mobiledrive All Rights Reserved

author : xiaolong.song
"""
from src.main.deviceMgt import DEVICEMGT
from src.main.requestUtil import HttpApi


def deviceInfoupdateDeviceInfoByDeviceId(param_data, token, environment):
    """
    根据系统设备ID更新设备信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/updateDeviceInfoByDeviceId", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplateupdateUserTemplate(param_data, token, environment):
    """
    用户设备模板-编辑更新/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/updateUserTemplate", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceServerSettingsaddEmailServerSettings(param_data, token, environment):
    """
    添加Email配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/addEmailServerSettings", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceServerSettingsdeleteServerSettingsBySettingId(param_data, token, environment):
    """
    根据配置Id删除配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/deleteServerSettingsBySettingId", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceServerSettingsupdateEmailServerSettingsBySettingId(param_data, token, environment):
    """
    根据配置Id更新Email配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/updateEmailServerSettingsBySettingId", DEVICEMGT())
    return HttpApi.post(http_api)


def managergetRuleChainMetaData(param_data, token, environment):
    """
    根据规则链id，获取规则链的节点、连接线详情/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/getRuleChainMetaData", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfogetConnectInfoByDeviceId(param_data, token, environment):
    """
    根据系统设备ID获取连接详情/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/getConnectInfoByDeviceId", DEVICEMGT())
    return HttpApi.get(http_api)


def labelDatagetNextLabelMarkData(param_data, token, environment):
    """
    取得下一筆審核資料/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/getNextLabelMarkData", DEVICEMGT())
    return HttpApi.post(http_api)


def sysRoleupdate(param_data, token, environment):
    """
    根据id更新系统角色信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysRole/update", DEVICEMGT())
    return HttpApi.put(http_api)


def deviceChannelRuleChainupdateRuleChain(param_data, token, environment):
    """
    修改一条规则链/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceChannelRuleChain/updateRuleChain", DEVICEMGT())
    return HttpApi.post(http_api)


def managersaveRuleChainMetaData(param_data, token, environment):
    """
    保存（或修改）规则链的节点、连接线详情/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/saveRuleChainMetaData", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUsergetById(param_data, token, environment):
    """
    根据id获取系统用户信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/{id}", DEVICEMGT())
    return HttpApi.get(http_api)


def sysUsergetUserByRoleId(param_data, token, environment):
    """
    根据角色查用户/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/getUserByRoleId", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfogetDeviceMqTopicByDeviceIdNo(param_data, token, environment):
    """
    根据设备ID编号，获取设备的mqtt主题列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/api/deviceInfo/getDeviceMqTopicByDeviceIdNo", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfodeleteDeviceByIds(param_data, token, environment):
    """
    根据系统设备ID删除设备/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/deleteDeviceByIds", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceEmailTemplategetEmailTemplateInfoById(param_data, token, environment):
    """
    根據模版ID獲取Email模版信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/getEmailTemplateInfoById", DEVICEMGT())
    return HttpApi.get(http_api)


def sysChannelUserupdateChannelUserByUserId(param_data, token, environment):
    """
    根据用户id更新渠道权限/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysChannelUser/updateChannelUserByUserId", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceChannelRuleChainpageQueryRuleChain(param_data, token, environment):
    """
    分页查询规则链列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceChannelRuleChain/pageQueryRuleChain", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfoselfRegisterDevice(param_data, token, environment):
    """
    自注册设备/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "device/device/deviceInfo/selfRegisterDevice", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceEmailTemplateupdateSysEmailTemplateInfoById(param_data, token, environment):
    """
    根據模版ID更新內置Email模版信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/updateSysEmailTemplateInfoById", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfoupdateDeviceStatus(param_data, token, environment):
    """
    更新设备状态/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/api/deviceInfo/updateDeviceStatus", DEVICEMGT())
    return HttpApi.post(http_api)


def managerfindNodeConfigByRuleChainIdAndType(param_data, token, environment):
    """
    根据规则链id，节点类型，查询同一类型节点的配置项/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/findNodeConfigByRuleChainIdAndType", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceEmailTemplatedeleteEmailTemplateInfoById(param_data, token, environment):
    """
    根據模版ID刪除Email模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/deleteEmailTemplateInfoById", DEVICEMGT())
    return HttpApi.get(http_api)


def labelMenucreateMenu(param_data, token, environment):
    """
    創建菜單/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelMenu/createMenu", DEVICEMGT())
    return HttpApi.get(http_api)


def manageraddRuleChain(param_data, token, environment):
    """
    新增规则链/r/n返回的data节点是规则链Id，有值即表示成功
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/addRuleChain", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceEmailTemplateselectEmailTemplateList(param_data, token, environment):
    """
    Email模版列表分頁查詢/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/selectEmailTemplateList", DEVICEMGT())
    return HttpApi.post(http_api)


def sysPermissionselectApiUrls(param_data, token, environment):
    """
    获取所有API URL/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/selectApiUrls", DEVICEMGT())
    return HttpApi.get(http_api)


def sysPermissionsave(param_data, token, environment):
    """
    新增系统权限/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/save", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplatequerySysTemplate(param_data, token, environment):
    """
    内置设备模板-查询列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/querySysTemplate", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUsergetAreaCodeList(param_data, token, environment):
    """
    获取手机区号列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/getAreaCodeList", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceContentTemplategetContentJson(param_data, token, environment):
    """
    用户（内置）设备模板-获取模板的json内容/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/getContentJson", DEVICEMGT())
    return HttpApi.get(http_api)


def labelDatagetLastLabelMarkData(param_data, token, environment):
    """
    取得上一筆審核資料/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/getLastLabelMarkData", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUsergetCurrentUserInfo(param_data, token, environment):
    """
    获取当前登录用户信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/getCurrentUserInfo", DEVICEMGT())
    return HttpApi.get(http_api)


def sysRolegetById(param_data, token, environment):
    """
    根据id获取系统角色信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysRole/{id}", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceDatagetFileConfig(param_data, token, environment):
    """
    获取规则链文件上传配置信息/r/n需要结合fus服务一起使用
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/device/deviceData/getFileConfig", DEVICEMGT())
    return HttpApi.get(http_api)


def sysUserforgetPassword(param_data, token, environment):
    """
    忘记密码-修改密码/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/forgetPassword", DEVICEMGT())
    return HttpApi.post(http_api)


def sysRoleassignUsers(param_data, token, environment):
    """
    给角色分配用户/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysRole/assignUsers", DEVICEMGT())
    return HttpApi.post(http_api)


def labelMenugetJourneyTimeMenuList(param_data, token, environment):
    """
    取得旅程時間菜單列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelMenu/getJourneyTimeMenuList", DEVICEMGT())
    return HttpApi.post(http_api)


def labelDatagetLabelMarkDataCount(param_data, token, environment):
    """
    取得審核資料數量/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/getLabelMarkDataCount", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplategetTemplateInfoForComponents(param_data, token, environment):
    """
    sms-email组件-获取模板列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/getTemplateInfoForComponents", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUserselectUserMenu(param_data, token, environment):
    """
    获取当前登录用户菜单/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/selectUserMenu", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfogetDeviceInfoByDeviceId(param_data, token, environment):
    """
    根据系统设备ID获取设备信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/getDeviceInfoByDeviceId", DEVICEMGT())
    return HttpApi.get(http_api)


def sysChannelUsergetChannelUserListByUserId(param_data, token, environment):
    """
    根据用户id查询关系渠道/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysChannelUser/getChannelUserListByUserId", DEVICEMGT())
    return HttpApi.get(http_api)


def sysPermissiongetById(param_data, token, environment):
    """
    根据id查询系统权限信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/{id}", DEVICEMGT())
    return HttpApi.get(http_api)


def payloadStructuredeviceStatusJsonToBase64(param_data, token, environment):
    """
    設備上下線JSON消息轉為base64字串/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/payloadStructure/deviceStatusJsonToBase64", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceProfileselect(param_data, token, environment):
    """
    设备配置分页查询/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/select", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplateupdateSMSTemplateInfoById(param_data, token, environment):
    """
    根據模版ID更新短信模版信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/updateSMSTemplateInfoById", DEVICEMGT())
    return HttpApi.post(http_api)


def rpcdeviceCloudRequest(param_data, token, environment):
    """
    云端请求-异步，需等待返回结果，判断http Code=200/r/n返回结果的data节点，true：表示请求成功，false：请求失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/rpc/deviceCloudRequest", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfodisconnectByClientId(param_data, token, environment):
    """
    根据clientId使client断开连接/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/disconnectByClientId", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceSMSTemplatesaveSMSTemplateInfo(param_data, token, environment):
    """
    添加短信模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/saveSMSTemplateInfo", DEVICEMGT())
    return HttpApi.post(http_api)


def sysRolesave(param_data, token, environment):
    """
    新增系统角色/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysRole/save", DEVICEMGT())
    return HttpApi.post(http_api)


def sysRoleselectPage(param_data, token, environment):
    """
    分页查询系统角色/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysRole/selectPage", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceProfileedit(param_data, token, environment):
    """
    更新配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/edit", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceChannelRuleChaincountByChannelIdAndChannelModelId(param_data, token, environment):
    """
    根据渠道id、类别id，统计渠道规则链数量/r/n返回的data节点的含义：具体数量
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceChannelRuleChain/countByChannelIdAndChannelModelId", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceEmailTemplatesaveEmailTemplateInfo(param_data, token, environment):
    """
    添加Email模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/saveEmailTemplateInfo", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfogetSuccessConnectedDeviceNum(param_data, token, environment):
    """
    获取成功连接数/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/getSuccessConnectedDeviceNum", DEVICEMGT())
    return HttpApi.get(http_api)


def alarmlistByOriginatorId(param_data, token, environment):
    """
    查询设备所有报警/r/n注意：1、若设备之前已有激活的同类型警报，再次发相同警报时，不会创建一条新警报，只会更新警报的结束时间；<br />2、若无激活的同类型警报，才会创建一条新警报；
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/alarm/listByOriginatorId", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceProfilegetById(param_data, token, environment):
    """
    设备配置详情/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/getById", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfogetDeviceRuleChainByDeviceCredentialsKey(param_data, token, environment):
    """
    根据设备的身份验证key，获取设备规则链信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/api/deviceInfo/getDeviceRuleChainByDeviceCredentialsKey", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceProfileadd(param_data, token, environment):
    """
    添加配置/r/n返回结果的data节点是设备配置id
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/add", DEVICEMGT())
    return HttpApi.post(http_api)


def nodeConfigcreateAlarmNode(param_data, token, environment):
    """
    create alarm（创建报警组件的配置）/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/nodeConfig/createAlarmNode", DEVICEMGT())
    return HttpApi.get(http_api)


def sysUsergetSmsCode(param_data, token, environment):
    """
    获取手机验证码/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/getSmsCode", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfogetCurrentConnectDeviceNum(param_data, token, environment):
    """
    获取当前连接数/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/getCurrentConnectDeviceNum", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceSMSTemplatedeleteSMSTemplateInfoById(param_data, token, environment):
    """
    根據模版ID刪除短信模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/deleteSMSTemplateInfoById", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceSMSTemplategetSMSTemplateInfoById(param_data, token, environment):
    """
    根據模版ID獲取短信模版信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/getSMSTemplateInfoById", DEVICEMGT())
    return HttpApi.get(http_api)


def labelDatagetLabelMarkDataList(param_data, token, environment):
    """
    取得審核資料分頁查詢結果/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/getLabelMarkDataList", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplateinitUserTemplateData(param_data, token, environment):
    """
    用户设备模板-初始化设备配置、规则链等数据/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/initUserTemplateData", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplateaddUserTemplate(param_data, token, environment):
    """
    用户设备模板-添加/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/addUserTemplate", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceDataqueryDataViewConfigByDeviceId(param_data, token, environment):
    """
    根据设备id，查询所有数据展示组件的配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/device/deviceData/queryDataViewConfigByDeviceId", DEVICEMGT())
    return HttpApi.get(http_api)


def nodeConfigclearAlarmNode(param_data, token, environment):
    """
    clear alarm（清除报警组件的配置）/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/nodeConfig/clearAlarmNode", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceChannelRuleChainbatchDeleteRuleChain(param_data, token, environment):
    """
    根据规则链id，批量删除规则链/r/n返回的data节点的含义：true：删除成功，false: 删除失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceChannelRuleChain/batchDeleteRuleChain", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceChannelRuleChaingetByRuleChainId(param_data, token, environment):
    """
    根据规则链id，获取规则链的基本信息/r/n返回的data节点的含义：true：删除成功，false: 删除失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceChannelRuleChain/getByRuleChainId", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceProfileselectAll(param_data, token, environment):
    """
    查询渠道下所有设备配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/selectAll", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplateupdateSysSMSTemplateInfoById(param_data, token, environment):
    """
    根據模版ID更新內置短信模版信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/updateSysSMSTemplateInfoById", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceServerSettingsgetSettingsForComponents(param_data, token, environment):
    """
    sms-email组件-获取配置列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/getSettingsForComponents", DEVICEMGT())
    return HttpApi.post(http_api)


def labelDataupdateLabelMarkData(param_data, token, environment):
    """
    更新審核資料/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/updateLabelMarkData", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceEmailTemplatesaveSysEmailTemplateInfo(param_data, token, environment):
    """
    添加內置Email模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/saveSysEmailTemplateInfo", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUserupdate(param_data, token, environment):
    """
    更新系统用户信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/update", DEVICEMGT())
    return HttpApi.put(http_api)


def deviceInfoaddDevice(param_data, token, environment):
    """
    添加设备/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/addDevice", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceProfiledelbatch(param_data, token, environment):
    """
    批量删除配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/delbatch", DEVICEMGT())
    return HttpApi.post(http_api)


def payloadStructureconvertJson(param_data, token, environment):
    """
    将其它格式的报文模板转换为json结构/r/ndata节点便是完整的json结构，注意：因protocol解析受限，返回的json都以对象表示，没表示出数组，但字段都在
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/payloadStructure/convertJson", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUserupdateUserInfoById(param_data, token, environment):
    """
    根据id修改用户信息，包括状态或密码/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/updateUserInfoById", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfogetDeviceRuleChainByDeviceId(param_data, token, environment):
    """
    根据设备id，获取设备规则链信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/api/deviceInfo/getDeviceRuleChainByDeviceId", DEVICEMGT())
    return HttpApi.get(http_api)


def labelMenugetDeviceMenuList(param_data, token, environment):
    """
    取得設備菜單列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelMenu/getDeviceMenuList", DEVICEMGT())
    return HttpApi.post(http_api)


def sysPermissionselectTreeMenu(param_data, token, environment):
    """
    获取树形菜单/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/selectTreeMenu", DEVICEMGT())
    return HttpApi.get(http_api)


def managergetRuleChainById(param_data, token, environment):
    """
    根据规则链id，获取规则链基础信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/getRuleChainById", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceNodeConfigDescpushNode(param_data, token, environment):
    """
    推送组件-配置类/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceNodeConfigDesc/pushNode", DEVICEMGT())
    return HttpApi.get(http_api)


def sysChannelUsergetCurrentUserChannelList(param_data, token, environment):
    """
    获取当前用户绑定的渠道/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysChannelUser/getCurrentUserChannelList", DEVICEMGT())
    return HttpApi.get(http_api)


def sysUserdeleteAccount(param_data, token, environment):
    """
    销户/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/deleteAccount", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceEmailTemplatedeleteSysEmailTemplateInfoById(param_data, token, environment):
    """
    根據模版ID刪除內置Email模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/deleteSysEmailTemplateInfoById", DEVICEMGT())
    return HttpApi.get(http_api)


def sysChannelUserselectUserList(param_data, token, environment):
    """
    用户查询列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysChannelUser/selectUserList", DEVICEMGT())
    return HttpApi.get(http_api)


def componentgetComponentDescriptorByClazz(param_data, token, environment):
    """
    根据组件类名，获取组件详情/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/component/getComponentDescriptorByClazz", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceServerSettingsselectPage(param_data, token, environment):
    """
    配置列表分页查询/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/selectPage", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplateselectSysSMSTemplateList(param_data, token, environment):
    """
    內置短信模版列表分頁查詢/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/selectSysSMSTemplateList", DEVICEMGT())
    return HttpApi.post(http_api)


def sysPermissiondelete(param_data, token, environment):
    """
    删除系统权限/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/delete", DEVICEMGT())
    return HttpApi.delete(http_api)


def deviceServerSettingsgetServerSettingsInfoBySettingId(param_data, token, environment):
    """
    根据配置Id获取配置详情/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/getServerSettingsInfoBySettingId", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceInfoinvalidateSessionByClientId(param_data, token, environment):
    """
    根据clientId使client session失效/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/invalidateSessionByClientId", DEVICEMGT())
    return HttpApi.get(http_api)


def managerpageQueryRuleChains(param_data, token, environment):
    """
    分页查询规则链/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/pageQueryRuleChains", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUserresetPassword(param_data, token, environment):
    """
    重设密码/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/resetPassword", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplateaddSysTemplate(param_data, token, environment):
    """
    内置设备模板-添加/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/addSysTemplate", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceDatapageQueryData(param_data, token, environment):
    """
    分页查询设备数据/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/device/deviceData/pageQueryData", DEVICEMGT())
    return HttpApi.post(http_api)


def managerupdateRuleChain(param_data, token, environment):
    """
    修改规则链/r/n返回的data节点是规则链Id，有值即表示成功
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/updateRuleChain", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplateupdateSysTemplate(param_data, token, environment):
    """
    内置设备模板-编辑更新/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/updateSysTemplate", DEVICEMGT())
    return HttpApi.post(http_api)


def labelDatagetLabelMarkData(param_data, token, environment):
    """
    取得審核資料/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/getLabelMarkData", DEVICEMGT())
    return HttpApi.get(http_api)


def labelDatagetJourneyAuthority(param_data, token, environment):
    """
    取得旅程審核權/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelData/getJourneyAuthority", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplatesaveSysSMSTemplateInfo(param_data, token, environment):
    """
    添加內置短信模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/saveSysSMSTemplateInfo", DEVICEMGT())
    return HttpApi.post(http_api)


def nodeConfigmongodbNode(param_data, token, environment):
    """
    MongoDb组件的配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/nodeConfig/mongodbNode", DEVICEMGT())
    return HttpApi.get(http_api)


def managerdeleteRuleChain(param_data, token, environment):
    """
    删除规则链/r/n返回的data节点：true表示删除成功，false表示失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/deleteRuleChain", DEVICEMGT())
    return HttpApi.get(http_api)


def sysUserrevokeDeleteAccount(param_data, token, environment):
    """
    撤销销户/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/revokeDeleteAccount", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUserselectPage(param_data, token, environment):
    """
    分页查询系统用户/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/selectPage", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceChannelRuleChainaddRuleChain(param_data, token, environment):
    """
    添加一条规则链/r/n返回的data节点是：规则链id，唯一主键
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/deviceChannelRuleChain/addRuleChain", DEVICEMGT())
    return HttpApi.post(http_api)


def sysUsergetSysServiceList(param_data, token, environment):
    """
    获取服务列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/getSysServiceList", DEVICEMGT())
    return HttpApi.get(http_api)


def labelMenugetJourneyDateMenuList(param_data, token, environment):
    """
    取得旅程日期菜單列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelMenu/getJourneyDateMenuList", DEVICEMGT())
    return HttpApi.post(http_api)


def sysRoledelete(param_data, token, environment):
    """
    删除系统角色/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysRole/delete", DEVICEMGT())
    return HttpApi.delete(http_api)


def sysUseradminResetPassword(param_data, token, environment):
    """
    用户修改密码/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/adminResetPassword", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceProfiledelById(param_data, token, environment):
    """
    删除配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceProfile/del", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceEmailTemplateselectSysEmailTemplateList(param_data, token, environment):
    """
    內置Email模版列表分頁查詢/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/selectSysEmailTemplateList", DEVICEMGT())
    return HttpApi.post(http_api)


def labelMenuupdateJourneyStatus(param_data, token, environment):
    """
    更新旅程審核狀態/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/labelMenu/updateJourneyStatus", DEVICEMGT())
    return HttpApi.post(http_api)


def convertFileaddJsonFiles(param_data, token, environment):
    """
    将S3文件存到MySQL/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "biomatics/dashboard/convertFile/addJsonFiles", DEVICEMGT())
    return HttpApi.post(http_api)


def labelDatagetLabelMarkDataForCli(param_data, token, environment):
    """
    取得LabelMarkData資料/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "label/api/labelData/getLabelMarkDataForCli", DEVICEMGT())
    return HttpApi.post(http_api)


def trustedAuthgetTicket(param_data, token, environment):
    """
    获取信任票证/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "biomatics/dashboard/trustedAuth/getTicket", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplatequeryUserTemplate(param_data, token, environment):
    """
    用户设备模板-查询列表/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/queryUserTemplate", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplatedeleteSysSMSTemplateInfoById(param_data, token, environment):
    """
    根據模版ID刪除內置短信模版/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/deleteSysSMSTemplateInfoById", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfogetAllDeviceNum(param_data, token, environment):
    """
    获取总设备数/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/getAllDeviceNum", DEVICEMGT())
    return HttpApi.get(http_api)


def payloadStructurejsonToBase64(param_data, token, environment):
    """
    動態將JSON消息轉為base64字串/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/payloadStructure/jsonToBase64", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceEmailTemplateupdateEmailTemplateInfoById(param_data, token, environment):
    """
    根據模版ID更新Email模版信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceEmailTemplate/updateEmailTemplateInfoById", DEVICEMGT())
    return HttpApi.post(http_api)


def engineruleStart(param_data, token, environment):
    """
    运行某条规则链/r/n返回结果的data节点，true：运行成功，false：运行失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/engine/ruleStart", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceProfilecountByRuleChainId(param_data, token, environment):
    """
    统计使用了该规则链的设备配置数量/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/api/deviceProfile/countByRuleChainId", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceServerSettingsaddSmsServerSettings(param_data, token, environment):
    """
    添加短信配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/addSmsServerSettings", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceSMSTemplateselectSMSTemplateList(param_data, token, environment):
    """
    短信模版列表分頁查詢/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceSMSTemplate/selectSMSTemplateList", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplategetInitDefaultValueVo(param_data, token, environment):
    """
    用户（内置）设备模板-获取初始化时必填项的默认值/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/getInitDefaultValueVo", DEVICEMGT())
    return HttpApi.get(http_api)


def sysPermissionupdate(param_data, token, environment):
    """
    根据id更新系统权限信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/update", DEVICEMGT())
    return HttpApi.put(http_api)


def sysUsersave(param_data, token, environment):
    """
    新增系统用户/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysUser/save", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceContentTemplatedeleteUserTemplate(param_data, token, environment):
    """
    用户设备模板-删除/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/deleteUserTemplate", DEVICEMGT())
    return HttpApi.get(http_api)


def sysPermissionselectPage(param_data, token, environment):
    """
    分页查询系统权限信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/sysuser/sysPermission/selectPage", DEVICEMGT())
    return HttpApi.get(http_api)


def componentlistAllComponent(param_data, token, environment):
    """
    查询所有的组件列表，并按类型分组/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/component/listAllComponent", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceContentTemplatedeleteSysTemplate(param_data, token, environment):
    """
    内置设备模板-删除/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/deleteSysTemplate", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceContentTemplateinitSysTemplateData(param_data, token, environment):
    """
    内置设备模板-初始化设备配置、规则链等数据/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/deviceContentTemplate/initSysTemplateData", DEVICEMGT())
    return HttpApi.post(http_api)


def alarmfindLatestByOriginatorAndType(param_data, token, environment):
    """
    查询设备最新的一条报警/r/n注意：1、若设备之前已有激活的同类型警报，再次发相同警报时，不会创建一条新警报，只会更新警报的结束时间；<br />2、若无激活的同类型警报，才会创建一条新警报；<br /> 3、该接口只返回创建时间最新的一条数据
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/alarm/findLatestByOriginatorAndType", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceDataqueryDataViewConfigByRuleChainId(param_data, token, environment):
    """
    根据规则链id，查询所有数据展示组件的配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/device/deviceData/queryDataViewConfigByRuleChainId", DEVICEMGT())
    return HttpApi.get(http_api)


def deviceInfoselectPage(param_data, token, environment):
    """
    设备列表分页查询/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceInfo/selectPage", DEVICEMGT())
    return HttpApi.post(http_api)


def deviceServerSettingsupdateSmsServerSettingsBySettingId(param_data, token, environment):
    """
    根据配置Id更新短信配置/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "admin/device/deviceServerSettings/updateSmsServerSettingsBySettingId", DEVICEMGT())
    return HttpApi.post(http_api)


def managerfindParentNode(param_data, token, environment):
    """
    获取指定类型父节点配置信息/r/n
    :param param_data: 接口请求参数:
                        
    :param token: 登录token
    :param environment: 环境参数
    :return:
    """
    http_api = HttpApi(param_data, token, environment, "rule/ruleChain/manager/findParentNode", DEVICEMGT())
    return HttpApi.get(http_api)


