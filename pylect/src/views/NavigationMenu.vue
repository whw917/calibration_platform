<!-- NavigationMenu.vue -->

<template>
    <div style="display: flex; justify-content: space-between; align-items: left;">
        
        <Dropdown @on-click="handleClick">
            <Icon type="ios-menu-outline" size="24"></Icon>
            <DropdownMenu slot="list">

              <DropdownItem name="Home">
                <Icon type="md-home"></Icon>
                主页面
              </DropdownItem>

              <DropdownItem name="ProcessManagement">
                <Icon type="md-settings"></Icon>
                流程管理
              </DropdownItem>

              <DropdownItem name="DataSearch">
                <Icon type="md-settings"></Icon>
                数据查询
              </DropdownItem>

              <DropdownItem name="ReportManagement">
                <Icon type="md-settings"></Icon>
                标定报告
              </DropdownItem>

              <DropdownItem name="LogManagement">
                <Icon type="md-settings"></Icon>
                日志管理
              </DropdownItem>

              <DropdownItem name="SystemParameter">
                <Icon type="md-settings"></Icon>
                参数设置
              </DropdownItem>
            
              <DropdownItem name="UpdatePassword">
                <Icon type="md-settings"></Icon>
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

            case 'ProcessManagement':
            this.$router.push('/process-management'); 
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
  