# Xunit Test:
    - This is the way of the testing that is being done in which there exists the methods as of such setup and the teardown method

    - This executes the code before and after the Modules, Functions, Classes and the Methods

       * Test Modules:
         - They could be used to test the modules withe the methods before the module being called and with the methods of after the moudule being called .
         Examples:
         ```

            def setup_module():
            def teardown_module():

         ```
       * Test Function:
         - They could be used to test the modules withe the methods before the  `TestFunction` being called and with the methods of after the `Test Function` being called .
        ```
          def setup_function():
          def teardown_function():
        ```

       * Test Classes:
        - They could be used to test the modules withe the methods before the `Class`  being called and with the methods of after the `Class` being called .
        ```          
            def setup_class():
            def teardown_class():
        ```

       * To wrap the test methods we have
        ```
            def setup_method():
            def teardown_method():
        ```


The following are the set of the setup and the teardown methods that exist
