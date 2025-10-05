class Solution:
    def simplifyPath(self, path: str) -> str:
        directory_stack = []
        path_components = path.split('/')      
        for component in path_components:
            
            if not component or component == '.':
                continue
          
            
            if component == '..':
                
                if directory_stack:
                    directory_stack.pop()
            else:
                
                directory_stack.append(component)
      

        simplified_path = '/' + '/'.join(directory_stack)
      
        return simplified_path

                            
                        
                
                
                
