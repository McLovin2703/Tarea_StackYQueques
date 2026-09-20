class Solution(object):
    def inorderTraversal(self, root):
        resultado = []

        def recorrer(nodo):
            if nodo is None:
                return

            recorrer(nodo.left)
            resultado.append(nodo.val)
            recorrer(nodo.right)

        recorrer(root)

        return resultado