import React from "react";
import {
  MailOutlined,
  SettingOutlined,
  NumberOutlined,
  NotificationOutlined,
  EditOutlined
} from "@ant-design/icons";

const mail = () => <MailOutlined />;

const notice = () => <NotificationOutlined />;

const result = () => <NumberOutlined />;

const manage = () => <SettingOutlined />;

const edit = () => <EditOutlined />;

const icons = {
  mail: mail,
  result: result,
  notice: notice,
  manage: manage,
  edit: edit
};

export default icons;
