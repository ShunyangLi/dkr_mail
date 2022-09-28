import React from "react";
import {
  MailOutlined,
  SettingOutlined,
  NumberOutlined,
  NotificationOutlined
} from '@ant-design/icons';

const mail = () => (
    <MailOutlined />
);

const notice = () => (
    <NotificationOutlined />
);


const result = () => (
    <NumberOutlined />
);

const manage = () => (
    <SettingOutlined />
);

const icons = {
  mail: mail,
  result: result,
  notice: notice,
  manage: manage
};

export default icons;
