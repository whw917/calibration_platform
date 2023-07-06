import Vue from 'vue'
import Router from 'vue-router'

//导航栏目录
import Home from '@/views/home'
import DataSearch from '@/components/DataSearch/DataSearch.vue';
import LogManagement from '@/components/LogManagement/LogManagement.vue';
import ProcessManagement from '@/components/ProcessManagement/ProcessManagement.vue';
import ReportManagement from '@/components/ReportManagement/ReportManagement.vue';
import SystemParameter from '@/components/SystemParameter/SystemParameter.vue';
import UpdatePassword from '@/components/UpdatePassword/UpdatePassword.vue';
import TestPage from '@/components/TestPage.vue';

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
      path: '/process-management',
      name: 'ProcessManagement',
      component: ProcessManagement,
    },
    {
      path: '/test-page',
      name: 'TestPage',
      component: TestPage,
    }
  ]
})
