"""
Copyright @2022-01-17 Mobiledrive All Rights Reserved

author : xiaolong.song
"""
import sys

import pytest

from src.main import pytest_assert
from src.main.common.testCaseAnalysis import test_case_analysis
from src.main.deviceMgt import DEVICEMGT
from src.main.deviceMgt.deviceMgtApi import deviceInfoupdateDeviceInfoByDeviceId, \
    deviceContentTemplateupdateUserTemplate, deviceServerSettingsaddEmailServerSettings, \
    deviceServerSettingsdeleteServerSettingsBySettingId, deviceServerSettingsupdateEmailServerSettingsBySettingId, \
    managergetRuleChainMetaData, deviceInfogetConnectInfoByDeviceId, labelDatagetNextLabelMarkData, sysRoleupdate, \
    deviceChannelRuleChainupdateRuleChain, managersaveRuleChainMetaData, sysUsergetById, sysUsergetUserByRoleId, \
    deviceInfogetDeviceMqTopicByDeviceIdNo, deviceInfodeleteDeviceByIds, deviceEmailTemplategetEmailTemplateInfoById, \
    sysChannelUserupdateChannelUserByUserId, deviceChannelRuleChainpageQueryRuleChain, deviceInfoselfRegisterDevice, \
    deviceEmailTemplateupdateSysEmailTemplateInfoById, deviceInfoupdateDeviceStatus, \
    managerfindNodeConfigByRuleChainIdAndType, deviceEmailTemplatedeleteEmailTemplateInfoById, labelMenucreateMenu, \
    manageraddRuleChain, deviceEmailTemplateselectEmailTemplateList, sysPermissionselectApiUrls, sysPermissionsave, \
    deviceContentTemplatequerySysTemplate, sysUsergetAreaCodeList, deviceContentTemplategetContentJson, \
    labelDatagetLastLabelMarkData, sysUsergetCurrentUserInfo, sysRolegetById, deviceDatagetFileConfig, \
    sysUserforgetPassword, sysRoleassignUsers, labelMenugetJourneyTimeMenuList, labelDatagetLabelMarkDataCount, \
    deviceSMSTemplategetTemplateInfoForComponents, sysUserselectUserMenu, deviceInfogetDeviceInfoByDeviceId, \
    sysChannelUsergetChannelUserListByUserId, sysPermissiongetById, payloadStructuredeviceStatusJsonToBase64, \
    deviceProfileselect, deviceSMSTemplateupdateSMSTemplateInfoById, rpcdeviceCloudRequest, \
    deviceInfodisconnectByClientId, deviceSMSTemplatesaveSMSTemplateInfo, sysRolesave, sysRoleselectPage, \
    deviceProfileedit, deviceChannelRuleChaincountByChannelIdAndChannelModelId, \
    deviceEmailTemplatesaveEmailTemplateInfo, deviceInfogetSuccessConnectedDeviceNum, alarmlistByOriginatorId, \
    deviceProfilegetById, deviceInfogetDeviceRuleChainByDeviceCredentialsKey, deviceProfileadd, \
    nodeConfigcreateAlarmNode, sysUsergetSmsCode, deviceInfogetCurrentConnectDeviceNum, \
    deviceSMSTemplatedeleteSMSTemplateInfoById, deviceSMSTemplategetSMSTemplateInfoById, labelDatagetLabelMarkDataList, \
    deviceContentTemplateinitUserTemplateData, deviceContentTemplateaddUserTemplate, \
    deviceDataqueryDataViewConfigByDeviceId, nodeConfigclearAlarmNode, deviceChannelRuleChainbatchDeleteRuleChain, \
    deviceChannelRuleChaingetByRuleChainId, deviceProfileselectAll, deviceSMSTemplateupdateSysSMSTemplateInfoById, \
    deviceServerSettingsgetSettingsForComponents, labelDataupdateLabelMarkData, \
    deviceEmailTemplatesaveSysEmailTemplateInfo, sysUserupdate, deviceInfoaddDevice, deviceProfiledelbatch, \
    payloadStructureconvertJson, sysUserupdateUserInfoById, deviceInfogetDeviceRuleChainByDeviceId, \
    labelMenugetDeviceMenuList, sysPermissionselectTreeMenu, managergetRuleChainById, deviceNodeConfigDescpushNode, \
    sysChannelUsergetCurrentUserChannelList, sysUserdeleteAccount, deviceEmailTemplatedeleteSysEmailTemplateInfoById, \
    sysChannelUserselectUserList, componentgetComponentDescriptorByClazz, deviceServerSettingsselectPage, \
    deviceSMSTemplateselectSysSMSTemplateList, sysPermissiondelete, \
    deviceServerSettingsgetServerSettingsInfoBySettingId, deviceInfoinvalidateSessionByClientId, \
    managerpageQueryRuleChains, sysUserresetPassword, deviceContentTemplateaddSysTemplate, deviceDatapageQueryData, \
    managerupdateRuleChain, deviceContentTemplateupdateSysTemplate, labelDatagetLabelMarkData, \
    labelDatagetJourneyAuthority, deviceSMSTemplatesaveSysSMSTemplateInfo, nodeConfigmongodbNode, \
    managerdeleteRuleChain, sysUserrevokeDeleteAccount, sysUserselectPage, deviceChannelRuleChainaddRuleChain, \
    sysUsergetSysServiceList, labelMenugetJourneyDateMenuList, sysRoledelete, sysUseradminResetPassword, \
    deviceProfiledelById, deviceEmailTemplateselectSysEmailTemplateList, labelMenuupdateJourneyStatus, \
    convertFileaddJsonFiles, labelDatagetLabelMarkDataForCli, trustedAuthgetTicket, \
    deviceContentTemplatequeryUserTemplate, deviceSMSTemplatedeleteSysSMSTemplateInfoById, deviceInfogetAllDeviceNum, \
    payloadStructurejsonToBase64, deviceEmailTemplateupdateEmailTemplateInfoById, engineruleStart, \
    deviceProfilecountByRuleChainId, deviceServerSettingsaddSmsServerSettings, deviceSMSTemplateselectSMSTemplateList, \
    deviceContentTemplategetInitDefaultValueVo, sysPermissionupdate, sysUsersave, \
    deviceContentTemplatedeleteUserTemplate, sysPermissionselectPage, componentlistAllComponent, \
    deviceContentTemplatedeleteSysTemplate, deviceContentTemplateinitSysTemplateData, \
    alarmfindLatestByOriginatorAndType, deviceDataqueryDataViewConfigByRuleChainId, deviceInfoselectPage, \
    deviceServerSettingsupdateSmsServerSettingsBySettingId, managerfindParentNode
from src.main.ics.icsApi import login
from src.tests import api_result


@pytest.fixture(scope="session")
def ics_login(option_e):
    result = login(DEVICEMGT(), option_e)

    if isinstance(result, str):
        assert False, result
    else:
        return result


def test_deviceInfoupdateDeviceInfoByDeviceId(option_e, ics_login):
    """
    根据系统设备ID更新设备信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfoupdateDeviceInfoByDeviceId(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplateupdateUserTemplate(option_e, ics_login):
    """
    用户设备模板-编辑更新/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplateupdateUserTemplate(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsaddEmailServerSettings(option_e, ics_login):
    """
    添加Email配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsaddEmailServerSettings(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsdeleteServerSettingsBySettingId(option_e, ics_login):
    """
    根据配置Id删除配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsdeleteServerSettingsBySettingId(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsupdateEmailServerSettingsBySettingId(option_e, ics_login):
    """
    根据配置Id更新Email配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsupdateEmailServerSettingsBySettingId(case, ics_login.access_token, option_e), param_key)


def test_managergetRuleChainMetaData(option_e, ics_login):
    """
    根据规则链id，获取规则链的节点、连接线详情/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managergetRuleChainMetaData(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetConnectInfoByDeviceId(option_e, ics_login):
    """
    根据系统设备ID获取连接详情/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetConnectInfoByDeviceId(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetNextLabelMarkData(option_e, ics_login):
    """
    取得下一筆審核資料/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetNextLabelMarkData(case, ics_login.access_token, option_e), param_key)


def test_sysRoleupdate(option_e, ics_login):
    """
    根据id更新系统角色信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysRoleupdate(case, ics_login.access_token, option_e), param_key)


def test_deviceChannelRuleChainupdateRuleChain(option_e, ics_login):
    """
    修改一条规则链/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceChannelRuleChainupdateRuleChain(case, ics_login.access_token, option_e), param_key)


def test_managersaveRuleChainMetaData(option_e, ics_login):
    """
    保存（或修改）规则链的节点、连接线详情/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managersaveRuleChainMetaData(case, ics_login.access_token, option_e), param_key)


def test_sysUsergetById(option_e, ics_login):
    """
    根据id获取系统用户信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsergetById(case, ics_login.access_token, option_e), param_key)


def test_sysUsergetUserByRoleId(option_e, ics_login):
    """
    根据角色查用户/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsergetUserByRoleId(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetDeviceMqTopicByDeviceIdNo(option_e, ics_login):
    """
    根据设备ID编号，获取设备的mqtt主题列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetDeviceMqTopicByDeviceIdNo(case, ics_login.access_token, option_e), param_key)


def test_deviceInfodeleteDeviceByIds(option_e, ics_login):
    """
    根据系统设备ID删除设备/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    #test_deviceInfoselectPage(option_e, ics_login)
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfodeleteDeviceByIds(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplategetEmailTemplateInfoById(option_e, ics_login):
    """
    根據模版ID獲取Email模版信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplategetEmailTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_sysChannelUserupdateChannelUserByUserId(option_e, ics_login):
    """
    根据用户id更新渠道权限/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysChannelUserupdateChannelUserByUserId(case, ics_login.access_token, option_e), param_key)


def test_deviceChannelRuleChainpageQueryRuleChain(option_e, ics_login):
    """
    分页查询规则链列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceChannelRuleChainpageQueryRuleChain(case, ics_login.access_token, option_e), param_key)


def test_deviceInfoselfRegisterDevice(option_e, ics_login):
    """
    自注册设备/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    # test_deviceProfileselect(option_e, ics_login)
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfoselfRegisterDevice(case, ics_login.access_token, option_e), param_key)
    # test_deviceInfodeleteDeviceByIds(option_e, ics_login)


def test_deviceEmailTemplateupdateSysEmailTemplateInfoById(option_e, ics_login):
    """
    根據模版ID更新內置Email模版信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplateupdateSysEmailTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_deviceInfoupdateDeviceStatus(option_e, ics_login):
    """
    更新设备状态/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfoupdateDeviceStatus(case, ics_login.access_token, option_e), param_key)


def test_managerfindNodeConfigByRuleChainIdAndType(option_e, ics_login):
    """
    根据规则链id，节点类型，查询同一类型节点的配置项/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managerfindNodeConfigByRuleChainIdAndType(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplatedeleteEmailTemplateInfoById(option_e, ics_login):
    """
    根據模版ID刪除Email模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplatedeleteEmailTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_labelMenucreateMenu(option_e, ics_login):
    """
    創建菜單/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelMenucreateMenu(case, ics_login.access_token, option_e), param_key)


def test_manageraddRuleChain(option_e, ics_login):
    """
    新增规则链/r/n返回的data节点是规则链Id，有值即表示成功
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(manageraddRuleChain(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplateselectEmailTemplateList(option_e, ics_login):
    """
    Email模版列表分頁查詢/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplateselectEmailTemplateList(case, ics_login.access_token, option_e), param_key)


def test_sysPermissionselectApiUrls(option_e, ics_login):
    """
    获取所有API URL/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissionselectApiUrls(case, ics_login.access_token, option_e), param_key)


def test_sysPermissionsave(option_e, ics_login):
    """
    新增系统权限/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissionsave(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplatequerySysTemplate(option_e, ics_login):
    """
    内置设备模板-查询列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplatequerySysTemplate(case, ics_login.access_token, option_e), param_key)


def test_sysUsergetAreaCodeList(option_e, ics_login):
    """
    获取手机区号列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsergetAreaCodeList(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplategetContentJson(option_e, ics_login):
    """
    用户（内置）设备模板-获取模板的json内容/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplategetContentJson(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetLastLabelMarkData(option_e, ics_login):
    """
    取得上一筆審核資料/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetLastLabelMarkData(case, ics_login.access_token, option_e), param_key)


def test_sysUsergetCurrentUserInfo(option_e, ics_login):
    """
    获取当前登录用户信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsergetCurrentUserInfo(case, ics_login.access_token, option_e), param_key)


def test_sysRolegetById(option_e, ics_login):
    """
    根据id获取系统角色信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysRolegetById(case, ics_login.access_token, option_e), param_key)


def test_deviceDatagetFileConfig(option_e, ics_login):
    """
    获取规则链文件上传配置信息/r/n需要结合fus服务一起使用
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceDatagetFileConfig(case, ics_login.access_token, option_e), param_key)


def test_sysUserforgetPassword(option_e, ics_login):
    """
    忘记密码-修改密码/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserforgetPassword(case, ics_login.access_token, option_e), param_key)


def test_sysRoleassignUsers(option_e, ics_login):
    """
    给角色分配用户/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysRoleassignUsers(case, ics_login.access_token, option_e), param_key)


def test_labelMenugetJourneyTimeMenuList(option_e, ics_login):
    """
    取得旅程時間菜單列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelMenugetJourneyTimeMenuList(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetLabelMarkDataCount(option_e, ics_login):
    """
    取得審核資料數量/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetLabelMarkDataCount(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplategetTemplateInfoForComponents(option_e, ics_login):
    """
    sms-email组件-获取模板列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplategetTemplateInfoForComponents(case, ics_login.access_token, option_e), param_key)


def test_sysUserselectUserMenu(option_e, ics_login):
    """
    获取当前登录用户菜单/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserselectUserMenu(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetDeviceInfoByDeviceId(option_e, ics_login):
    """
    根据系统设备ID获取设备信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetDeviceInfoByDeviceId(case, ics_login.access_token, option_e), param_key)


def test_sysChannelUsergetChannelUserListByUserId(option_e, ics_login):
    """
    根据用户id查询关系渠道/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysChannelUsergetChannelUserListByUserId(case, ics_login.access_token, option_e), param_key)


def test_sysPermissiongetById(option_e, ics_login):
    """
    根据id查询系统权限信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissiongetById(case, ics_login.access_token, option_e), param_key)


def test_payloadStructuredeviceStatusJsonToBase64(option_e, ics_login):
    """
    設備上下線JSON消息轉為base64字串/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(payloadStructuredeviceStatusJsonToBase64(case, ics_login.access_token, option_e), param_key)


def test_deviceProfileselect(option_e, ics_login):
    """
    设备配置分页查询/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfileselect(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplateupdateSMSTemplateInfoById(option_e, ics_login):
    """
    根據模版ID更新短信模版信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplateupdateSMSTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_rpcdeviceCloudRequest(option_e, ics_login):
    """
    云端请求-异步，需等待返回结果，判断http Code=200/r/n返回结果的data节点，true：表示请求成功，false：请求失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(rpcdeviceCloudRequest(case, ics_login.access_token, option_e), param_key)


def test_deviceInfodisconnectByClientId(option_e, ics_login):
    """
    根据clientId使client断开连接/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfodisconnectByClientId(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplatesaveSMSTemplateInfo(option_e, ics_login):
    """
    添加短信模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplatesaveSMSTemplateInfo(case, ics_login.access_token, option_e), param_key)


def test_sysRolesave(option_e, ics_login):
    """
    新增系统角色/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysRolesave(case, ics_login.access_token, option_e), param_key)


def test_sysRoleselectPage(option_e, ics_login):
    """
    分页查询系统角色/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysRoleselectPage(case, ics_login.access_token, option_e), param_key)


def test_deviceProfileedit(option_e, ics_login):
    """
    更新配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfileedit(case, ics_login.access_token, option_e), param_key)


def test_deviceChannelRuleChaincountByChannelIdAndChannelModelId(option_e, ics_login):
    """
    根据渠道id、类别id，统计渠道规则链数量/r/n返回的data节点的含义：具体数量
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceChannelRuleChaincountByChannelIdAndChannelModelId(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplatesaveEmailTemplateInfo(option_e, ics_login):
    """
    添加Email模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplatesaveEmailTemplateInfo(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetSuccessConnectedDeviceNum(option_e, ics_login):
    """
    获取成功连接数/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetSuccessConnectedDeviceNum(case, ics_login.access_token, option_e), param_key)


def test_alarmlistByOriginatorId(option_e, ics_login):
    """
    查询设备所有报警/r/n注意：1、若设备之前已有激活的同类型警报，再次发相同警报时，不会创建一条新警报，只会更新警报的结束时间；<br />2、若无激活的同类型警报，才会创建一条新警报；
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(alarmlistByOriginatorId(case, ics_login.access_token, option_e), param_key)


def test_deviceProfilegetById(option_e, ics_login):
    """
    设备配置详情/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfilegetById(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetDeviceRuleChainByDeviceCredentialsKey(option_e, ics_login):
    """
    根据设备的身份验证key，获取设备规则链信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetDeviceRuleChainByDeviceCredentialsKey(case, ics_login.access_token, option_e), param_key)


def test_deviceProfileadd(option_e, ics_login):
    """
    添加配置/r/n返回结果的data节点是设备配置id
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfileadd(case, ics_login.access_token, option_e), param_key)


def test_nodeConfigcreateAlarmNode(option_e, ics_login):
    """
    create alarm（创建报警组件的配置）/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(nodeConfigcreateAlarmNode(case, ics_login.access_token, option_e), param_key)


def test_sysUsergetSmsCode(option_e, ics_login):
    """
    获取手机验证码/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsergetSmsCode(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetCurrentConnectDeviceNum(option_e, ics_login):
    """
    获取当前连接数/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetCurrentConnectDeviceNum(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplatedeleteSMSTemplateInfoById(option_e, ics_login):
    """
    根據模版ID刪除短信模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplatedeleteSMSTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplategetSMSTemplateInfoById(option_e, ics_login):
    """
    根據模版ID獲取短信模版信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplategetSMSTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetLabelMarkDataList(option_e, ics_login):
    """
    取得審核資料分頁查詢結果/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetLabelMarkDataList(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplateinitUserTemplateData(option_e, ics_login):
    """
    用户设备模板-初始化设备配置、规则链等数据/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplateinitUserTemplateData(case, ics_login.access_token, option_e), param_key)
    #test_deviceInfodeleteDeviceByIds(option_e, ics_login)
    #test_deviceProfiledelById(option_e, ics_login)
    #test_deviceChannelRuleChainbatchDeleteRuleChain(option_e, ics_login)


def test_deviceContentTemplateaddUserTemplate(option_e, ics_login):
    """
    用户设备模板-添加/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplateaddUserTemplate(case, ics_login.access_token, option_e), param_key)


def test_deviceDataqueryDataViewConfigByDeviceId(option_e, ics_login):
    """
    根据设备id，查询所有数据展示组件的配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceDataqueryDataViewConfigByDeviceId(case, ics_login.access_token, option_e), param_key)


def test_nodeConfigclearAlarmNode(option_e, ics_login):
    """
    clear alarm（清除报警组件的配置）/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(nodeConfigclearAlarmNode(case, ics_login.access_token, option_e), param_key)



def test_deviceChannelRuleChainbatchDeleteRuleChain(option_e, ics_login):
    """
    根据规则链id，批量删除规则链/r/n返回的data节点的含义：true：删除成功，false: 删除失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    #test_deviceChannelRuleChainpageQueryRuleChain(option_e, ics_login)
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceChannelRuleChainbatchDeleteRuleChain(case, ics_login.access_token, option_e), param_key)


def test_deviceChannelRuleChaingetByRuleChainId(option_e, ics_login):
    """
    根据规则链id，获取规则链的基本信息/r/n返回的data节点的含义：true：删除成功，false: 删除失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceChannelRuleChaingetByRuleChainId(case, ics_login.access_token, option_e), param_key)


def test_deviceProfileselectAll(option_e, ics_login):
    """
    查询渠道下所有设备配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfileselectAll(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplateupdateSysSMSTemplateInfoById(option_e, ics_login):
    """
    根據模版ID更新內置短信模版信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplateupdateSysSMSTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsgetSettingsForComponents(option_e, ics_login):
    """
    sms-email组件-获取配置列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsgetSettingsForComponents(case, ics_login.access_token, option_e), param_key)


def test_labelDataupdateLabelMarkData(option_e, ics_login):
    """
    更新審核資料/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDataupdateLabelMarkData(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplatesaveSysEmailTemplateInfo(option_e, ics_login):
    """
    添加內置Email模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplatesaveSysEmailTemplateInfo(case, ics_login.access_token, option_e), param_key)


def test_sysUserupdate(option_e, ics_login):
    """
    更新系统用户信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserupdate(case, ics_login.access_token, option_e), param_key)


def test_deviceInfoaddDevice(option_e, ics_login):
    """
    添加设备/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfoaddDevice(case, ics_login.access_token, option_e), param_key)


def test_deviceProfiledelbatch(option_e, ics_login):
    """
    批量删除配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfiledelbatch(case, ics_login.access_token, option_e), param_key)


def test_payloadStructureconvertJson(option_e, ics_login):
    """
    将其它格式的报文模板转换为json结构/r/ndata节点便是完整的json结构，注意：因protocol解析受限，返回的json都以对象表示，没表示出数组，但字段都在
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(payloadStructureconvertJson(case, ics_login.access_token, option_e), param_key)


def test_sysUserupdateUserInfoById(option_e, ics_login):
    """
    根据id修改用户信息，包括状态或密码/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserupdateUserInfoById(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetDeviceRuleChainByDeviceId(option_e, ics_login):
    """
    根据设备id，获取设备规则链信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetDeviceRuleChainByDeviceId(case, ics_login.access_token, option_e), param_key)


def test_labelMenugetDeviceMenuList(option_e, ics_login):
    """
    取得設備菜單列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelMenugetDeviceMenuList(case, ics_login.access_token, option_e), param_key)


def test_sysPermissionselectTreeMenu(option_e, ics_login):
    """
    获取树形菜单/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissionselectTreeMenu(case, ics_login.access_token, option_e), param_key)


def test_managergetRuleChainById(option_e, ics_login):
    """
    根据规则链id，获取规则链基础信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managergetRuleChainById(case, ics_login.access_token, option_e), param_key)


def test_deviceNodeConfigDescpushNode(option_e, ics_login):
    """
    推送组件-配置类/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceNodeConfigDescpushNode(case, ics_login.access_token, option_e), param_key)


def test_sysChannelUsergetCurrentUserChannelList(option_e, ics_login):
    """
    获取当前用户绑定的渠道/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysChannelUsergetCurrentUserChannelList(case, ics_login.access_token, option_e), param_key)


def test_sysUserdeleteAccount(option_e, ics_login):
    """
    销户/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserdeleteAccount(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplatedeleteSysEmailTemplateInfoById(option_e, ics_login):
    """
    根據模版ID刪除內置Email模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplatedeleteSysEmailTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_sysChannelUserselectUserList(option_e, ics_login):
    """
    用户查询列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysChannelUserselectUserList(case, ics_login.access_token, option_e), param_key)


def test_componentgetComponentDescriptorByClazz(option_e, ics_login):
    """
    根据组件类名，获取组件详情/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(componentgetComponentDescriptorByClazz(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsselectPage(option_e, ics_login):
    """
    配置列表分页查询/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsselectPage(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplateselectSysSMSTemplateList(option_e, ics_login):
    """
    內置短信模版列表分頁查詢/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplateselectSysSMSTemplateList(case, ics_login.access_token, option_e), param_key)


def test_sysPermissiondelete(option_e, ics_login):
    """
    删除系统权限/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissiondelete(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsgetServerSettingsInfoBySettingId(option_e, ics_login):
    """
    根据配置Id获取配置详情/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsgetServerSettingsInfoBySettingId(case, ics_login.access_token, option_e), param_key)


def test_deviceInfoinvalidateSessionByClientId(option_e, ics_login):
    """
    根据clientId使client session失效/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfoinvalidateSessionByClientId(case, ics_login.access_token, option_e), param_key)


def test_managerpageQueryRuleChains(option_e, ics_login):
    """
    分页查询规则链/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managerpageQueryRuleChains(case, ics_login.access_token, option_e), param_key)


def test_sysUserresetPassword(option_e, ics_login):
    """
    重设密码/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserresetPassword(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplateaddSysTemplate(option_e, ics_login):
    """
    内置设备模板-添加/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplateaddSysTemplate(case, ics_login.access_token, option_e), param_key)


def test_deviceDatapageQueryData(option_e, ics_login):
    """
    分页查询设备数据/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceDatapageQueryData(case, ics_login.access_token, option_e), param_key)


def test_managerupdateRuleChain(option_e, ics_login):
    """
    修改规则链/r/n返回的data节点是规则链Id，有值即表示成功
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managerupdateRuleChain(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplateupdateSysTemplate(option_e, ics_login):
    """
    内置设备模板-编辑更新/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplateupdateSysTemplate(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetLabelMarkData(option_e, ics_login):
    """
    取得審核資料/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetLabelMarkData(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetJourneyAuthority(option_e, ics_login):
    """
    取得旅程審核權/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetJourneyAuthority(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplatesaveSysSMSTemplateInfo(option_e, ics_login):
    """
    添加內置短信模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplatesaveSysSMSTemplateInfo(case, ics_login.access_token, option_e), param_key)


def test_nodeConfigmongodbNode(option_e, ics_login):
    """
    MongoDb组件的配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(nodeConfigmongodbNode(case, ics_login.access_token, option_e), param_key)


def test_managerdeleteRuleChain(option_e, ics_login):
    """
    删除规则链/r/n返回的data节点：true表示删除成功，false表示失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managerdeleteRuleChain(case, ics_login.access_token, option_e), param_key)


def test_sysUserrevokeDeleteAccount(option_e, ics_login):
    """
    撤销销户/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserrevokeDeleteAccount(case, ics_login.access_token, option_e), param_key)


def test_sysUserselectPage(option_e, ics_login):
    """
    分页查询系统用户/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUserselectPage(case, ics_login.access_token, option_e), param_key)


def test_deviceChannelRuleChainaddRuleChain(option_e, ics_login):
    """
    添加一条规则链/r/n返回的data节点是：规则链id，唯一主键
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceChannelRuleChainaddRuleChain(case, ics_login.access_token, option_e), param_key)


def test_sysUsergetSysServiceList(option_e, ics_login):
    """
    获取服务列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsergetSysServiceList(case, ics_login.access_token, option_e), param_key)


def test_labelMenugetJourneyDateMenuList(option_e, ics_login):
    """
    取得旅程日期菜單列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelMenugetJourneyDateMenuList(case, ics_login.access_token, option_e), param_key)


def test_sysRoledelete(option_e, ics_login):
    """
    删除系统角色/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysRoledelete(case, ics_login.access_token, option_e), param_key)


def test_sysUseradminResetPassword(option_e, ics_login):
    """
    用户修改密码/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUseradminResetPassword(case, ics_login.access_token, option_e), param_key)


def test_deviceProfiledelById(option_e, ics_login):
    """
    删除配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    #test_deviceProfileselect(option_e, ics_login)
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfiledelById(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplateselectSysEmailTemplateList(option_e, ics_login):
    """
    內置Email模版列表分頁查詢/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplateselectSysEmailTemplateList(case, ics_login.access_token, option_e), param_key)


def test_labelMenuupdateJourneyStatus(option_e, ics_login):
    """
    更新旅程審核狀態/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelMenuupdateJourneyStatus(case, ics_login.access_token, option_e), param_key)


def test_convertFileaddJsonFiles(option_e, ics_login):
    """
    将S3文件存到MySQL/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(convertFileaddJsonFiles(case, ics_login.access_token, option_e), param_key)


def test_labelDatagetLabelMarkDataForCli(option_e, ics_login):
    """
    取得LabelMarkData資料/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(labelDatagetLabelMarkDataForCli(case, ics_login.access_token, option_e), param_key)


def test_trustedAuthgetTicket(option_e, ics_login):
    """
    获取信任票证/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(trustedAuthgetTicket(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplatequeryUserTemplate(option_e, ics_login):
    """
    用户设备模板-查询列表/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplatequeryUserTemplate(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplatedeleteSysSMSTemplateInfoById(option_e, ics_login):
    """
    根據模版ID刪除內置短信模版/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplatedeleteSysSMSTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_deviceInfogetAllDeviceNum(option_e, ics_login):
    """
    获取总设备数/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfogetAllDeviceNum(case, ics_login.access_token, option_e), param_key)


def test_payloadStructurejsonToBase64(option_e, ics_login):
    """
    動態將JSON消息轉為base64字串/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(payloadStructurejsonToBase64(case, ics_login.access_token, option_e), param_key)


def test_deviceEmailTemplateupdateEmailTemplateInfoById(option_e, ics_login):
    """
    根據模版ID更新Email模版信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceEmailTemplateupdateEmailTemplateInfoById(case, ics_login.access_token, option_e), param_key)


def test_engineruleStart(option_e, ics_login):
    """
    运行某条规则链/r/n返回结果的data节点，true：运行成功，false：运行失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(engineruleStart(case, ics_login.access_token, option_e), param_key)


def test_deviceProfilecountByRuleChainId(option_e, ics_login):
    """
    统计使用了该规则链的设备配置数量/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceProfilecountByRuleChainId(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsaddSmsServerSettings(option_e, ics_login):
    """
    添加短信配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsaddSmsServerSettings(case, ics_login.access_token, option_e), param_key)


def test_deviceSMSTemplateselectSMSTemplateList(option_e, ics_login):
    """
    短信模版列表分頁查詢/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceSMSTemplateselectSMSTemplateList(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplategetInitDefaultValueVo(option_e, ics_login):
    """
    用户（内置）设备模板-获取初始化时必填项的默认值/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplategetInitDefaultValueVo(case, ics_login.access_token, option_e), param_key)


def test_sysPermissionupdate(option_e, ics_login):
    """
    根据id更新系统权限信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissionupdate(case, ics_login.access_token, option_e), param_key)


def test_sysUsersave(option_e, ics_login):
    """
    新增系统用户/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysUsersave(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplatedeleteUserTemplate(option_e, ics_login):
    """
    用户设备模板-删除/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplatedeleteUserTemplate(case, ics_login.access_token, option_e), param_key)


def test_sysPermissionselectPage(option_e, ics_login):
    """
    分页查询系统权限信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(sysPermissionselectPage(case, ics_login.access_token, option_e), param_key)


def test_componentlistAllComponent(option_e, ics_login):
    """
    查询所有的组件列表，并按类型分组/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(componentlistAllComponent(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplatedeleteSysTemplate(option_e, ics_login):
    """
    内置设备模板-删除/r/n返回结果的data节点：true表示操作成功，false表示操作失败
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplatedeleteSysTemplate(case, ics_login.access_token, option_e), param_key)


def test_deviceContentTemplateinitSysTemplateData(option_e, ics_login):
    """
    内置设备模板-初始化设备配置、规则链等数据/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceContentTemplateinitSysTemplateData(case, ics_login.access_token, option_e), param_key)
    #test_deviceInfodeleteDeviceByIds(option_e, ics_login)
    #test_deviceProfiledelById(option_e, ics_login)
    #test_deviceChannelRuleChainbatchDeleteRuleChain(option_e, ics_login)


def test_alarmfindLatestByOriginatorAndType(option_e, ics_login):
    """
    查询设备最新的一条报警/r/n注意：1、若设备之前已有激活的同类型警报，再次发相同警报时，不会创建一条新警报，只会更新警报的结束时间；<br />2、若无激活的同类型警报，才会创建一条新警报；<br /> 3、该接口只返回创建时间最新的一条数据
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(alarmfindLatestByOriginatorAndType(case, ics_login.access_token, option_e), param_key)


def test_deviceDataqueryDataViewConfigByRuleChainId(option_e, ics_login):
    """
    根据规则链id，查询所有数据展示组件的配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceDataqueryDataViewConfigByRuleChainId(case, ics_login.access_token, option_e), param_key)


def test_deviceInfoselectPage(option_e, ics_login):
    """
    设备列表分页查询/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceInfoselectPage(case, ics_login.access_token, option_e), param_key)


def test_deviceServerSettingsupdateSmsServerSettingsBySettingId(option_e, ics_login):
    """
    根据配置Id更新短信配置/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(deviceServerSettingsupdateSmsServerSettingsBySettingId(case, ics_login.access_token, option_e), param_key)


def test_managerfindParentNode(option_e, ics_login):
    """
    获取指定类型父节点配置信息/r/n
    :param option_e: 环境参数，入test，pre等
    :param ics_login: ics登录信息，可以获取用户信息或者token
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)

    pytest_assert(managerfindParentNode(case, ics_login.access_token, option_e), param_key)


if __name__ == "__main__":
    pytest.main(["deviceMgtTest.py",
                 "-s",
                 "--e=test",
                 "--html=../../report/deviceMgtReport.html",
                 "--self-contained-html"])
