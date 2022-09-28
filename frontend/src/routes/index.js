import loadable from "@/utils/loadable";

const Index = loadable(() =>
  import(/* webpackChunkName: 'index' */ "@/views/Index")
);

const Manage = loadable(() =>
  import(/* webpackChunkName: 'index' */ "@/views/Manage")
);

const Notice = loadable(() =>
  import(/* webpackChunkName: 'index' */ "@/views/Notice")
);

const Result = loadable(() =>
  import(/* webpackChunkName: 'index' */ "@/views/Result")
);

const Edit = loadable(() =>
  import(/* webpackChunkName: 'index' */ "@/views/Edit")
);
const routes = [
  { path: "/index", exact: true, name: "Mail", component: Index },
  { path: "/result", exact: true, name: "Result", component: Result },
  { path: "/notice", exact: true, name: "Notice", component: Notice },
  { path: "/manage", exact: true, name: "Manage", component: Manage },
  { path: "/edit", exact: true, name: "Edit", component: Edit }
];

export default routes;
