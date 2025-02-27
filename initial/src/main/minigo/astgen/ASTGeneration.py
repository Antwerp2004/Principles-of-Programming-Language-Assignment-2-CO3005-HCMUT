from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # Program
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])

    # Declaration
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))
    
    # Statements
    def visitStmt(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))
    
    # Block
    def visitBlock(self,ctx:MiniGoParser.DeclContext):
        return Block([self.visit(x) for x in ctx.stmt()])
    	
    # Variable, Constant declaration
    def visitVar_decl(self,ctx:MiniGoParser.VardeclContext):
        return VarDecl(ctx.IDENTIFIER().getText(),
                       self.visit(ctx.decl_typ()) if ctx.decl_typ() else None,
                       self.visit(ctx.expr()) if ctx.expr() else None)
    
    def visitConst_decl(self,ctx:MiniGoParser.VardeclContext):
        return ConstDecl(ctx.IDENTIFIER().getText(), None, self.visit(ctx.expr()))
    
    def visitDecl_typ(self,ctx:MiniGoParser.Decl_typContext):
        return self.visit(ctx.getChild(0))
    
    # Assignment Statement
    def visitAssign_stmt(self,ctx:MiniGoParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        op = ctx.assign_operator().getText()
        if op == ':=':
            return Assign(lhs, rhs)
        else:
            return Assign(lhs, BinaryOp(op[0], lhs, rhs))
        
    def visitLhs(self,ctx:MiniGoParser.LhsContext):
        return self.visit(ctx.getChild(0))
    
    # If Statement
    def visitIf_stmt(self,ctx:MiniGoParser.If_stmtContext):
        return If(self.visit(ctx.only_if_stmt()) + self.visit(ctx.else_if_list()) + [self.visit(x) for x in ctx.else_stmt()])

    def visitFuncdecl(self,ctx:MiniGoParser.FuncdeclContext):
        return FuncDecl(ctx.ID().getText(),[],VoidType(),Block([]))