import Vue from 'vue'
import Router from 'vue-router'

//导航栏目录
import Home from '@/views/home'
import DataSearch from '@/components/DataSearch/DataSearch.vue';
import LogManagement from '@/components/LogManagement/LogManagement.vue';
import FlowManagement from '@/components/FlowManagement/FlowManagement.vue';
import ReportManagement from '@/components/ReportManagement/ReportManagement.vue';
import SystemParameter from '@/components/SystemParameter/SystemParameter.vue';
import UpdatePassword from '@/components/UpdatePassword/UpdatePassword.vue';
import TestPage from '@/components/TestPage.vue';

//其他页面导航
import ReportDetail from '@/components/ReportManagement/ReportDetail.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/data-search',
      name: 'DataSearch',
      component: DataSearch,
    },
    {
      path: '/system-parameter',
      name: 'SystemParameter',
      component: SystemParameter,
    },
    {
      path: '/log-management',
      name: 'LogManagement',
      component: LogManagement,
    },
    {
      path: '/report-management',
      name: 'ReportManagement',
      component: ReportManagement,
    },
    {
      path: '/update-password',
      name: 'UpdatePassword',
      component: UpdatePassword,
    },
    {
      path: '/flow-management',
      name: 'FlowManagement',
      component: FlowManagement,
    },
    {
      path: '/test-page',
      name: 'TestPage',
      component: TestPage,
    },


    {
      path: '/report-detail', // :id is a dynamic segment
      name: 'ReportDetail',
      component: ReportDetail,
      props: true, // Pass route.params to props
    },
    
  ]
})
