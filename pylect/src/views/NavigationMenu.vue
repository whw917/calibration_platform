<!-- NavigationMenu.vue -->

<template>
    <div style="display: flex; justify-content: space-between; align-items: left;">
        
        <Dropdown @on-click="handleClick">
            <Icon type="ios-menu-outline" size="24"></Icon>
            <DropdownMenu slot="list">

              <DropdownItem name="Home">
                <img :src="require('../images/main_page.png')" alt="home-icon" style="width: 13px; height: 13px;">
                主页面
              </DropdownItem>

              <DropdownItem name="FlowManagement">
                <img :src="require('../images/flow_management.png')" alt="home-icon" style="width: 13px; height: 13px;">
                流程管理
              </DropdownItem>

              <DropdownItem name="DataSearch">
                <img :src="require('../images/data_search.png')" alt="home-icon" style="width: 13px; height: 13px;">
                数据查询
              </DropdownItem>

              <DropdownItem name="ReportManagement">
                <img :src="require('../images/report_management.png')" alt="home-icon" style="width: 13px; height: 13px;">
                标定报告
              </DropdownItem>

              <DropdownItem name="LogManagement">
                <img :src="require('../images/log_management.png')" alt="home-icon" style="width: 13px; height: 13px;">
                日志管理
              </DropdownItem>

              <DropdownItem name="SystemParameter">
                <img :src="require('../images/parameter.png')" alt="home-icon" style="width: 13px; height: 13px;">
                参数设置
              </DropdownItem>
            
              <DropdownItem name="UpdatePassword">
                <img :src="require('../images/update_password.png')" alt="home-icon" style="width: 13px; height: 13px;">
                更改密码
              </DropdownItem>

              <DropdownItem name="TestPage">
                <Icon type="md-settings"></Icon>
                测试
              </DropdownItem>
              <!-- more menu items -->
            </DropdownMenu>
          </Dropdown>

      <div style="width: auto"></div>

    </div>
  </template>
  
  <script>
  export default {
    name: 'NavigationMenu',
    methods: {
      handleClick(name) {
        // Navigation logic
        switch (name) {
            case 'Home':
            this.$router.push('/'); // Go to Home page
            break;

            case 'FlowManagement':
            this.$router.push('/flow-management'); 
            break;

            case 'DataSearch':
            this.$router.push('/data-search'); 
            break;

            case 'ReportManagement':
            this.$router.push('/report-management'); 
            break;

            case 'LogManagement':
            this.$router.push('/log-management'); 
            break;

            case 'SystemParameter':
            this.$router.push('/system-parameter'); 
            break;

            case 'UpdatePassword':
            this.$router.push('/update-password'); 
            break;
            
            case 'TestPage':
            this.$router.push('/test-page'); 
            break;
            // Handle other cases
        }
      }
    }
  }
  </script>
  