import React, { Component } from "react";
import { Column } from '@ant-design/plots';
import CustomBreadcrumb from "@/components/CustomBreadcrumb/CustomBreadcrumb";
import "./index.scss";

const data = [
  {
    type: '家具家电',
    sales: 38,
  },
  {
    type: '粮油副食',
    sales: 52,
  },
  {
    type: '生鲜水果',
    sales: 61,
  },
  {
    type: '美容洗护',
    sales: 145,
  },
  {
    type: '母婴用品',
    sales: 48,
  },
  {
    type: '进口食品',
    sales: 38,
  },
  {
    type: '食品饮料',
    sales: 38,
  },
  {
    type: '家庭清洁',
    sales: 38,
  },
];
const config = {
  data,
  xField: 'type',
  yField: 'sales',
  label: {
    // 可手动配置 label 数据标签位置
    position: 'middle',
    // 'top', 'bottom', 'middle',
    // 配置样式
    style: {
      fill: '#FFFFFF',
      opacity: 0.6,
    },
  },
  xAxis: {
    label: {
      autoHide: true,
      autoRotate: false,
    },
  },
  meta: {
    type: {
      alias: '类别',
    },
    sales: {
      alias: '销售额',
    },
  },
};
class Result extends Component {
  constructor(props) {
    super(props);
    this.state = {
      search: "csv",
      loading: false,
      fileList: []
    };
  }


  render() {

    return (
      <div>
        <CustomBreadcrumb arr={["result"]} />
        <div style={{ width: "90%", marginTop: "5%", margin: "auto", top: 2, bottom: 0, left: 0, right: 0}}>
          <Column {...config} />
        </div>
      </div>
    );
  }
}

export default Result;
