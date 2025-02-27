from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):
    # Program
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])
    
    # Declaration
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))
    
    # Statements
    def visitStmt(self,ctx:MiniGoParser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    # Block
    def visitBlock(self,ctx:MiniGoParser.BlockContext):
        return Block([self.visit(x) for x in ctx.stmt()])
    	
    # Variable, Constant declaration
    def visitVar_decl(self,ctx:MiniGoParser.Var_declContext):
        return VarDecl(ctx.IDENTIFIER().getText(),
                       self.visit(ctx.typ()) if ctx.typ() else None,
                       self.visit(ctx.expr()) if ctx.expr() else None)
    
    def visitConst_decl(self,ctx:MiniGoParser.Const_declContext):
        return ConstDecl(ctx.IDENTIFIER().getText(), None, self.visit(ctx.expr()))
    
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
        x = self.visit(ctx.only_if_stmt())
        y = self.visit(ctx.else_if_list())[::-1] + [x]
        z = self.visit(ctx.else_stmt()) if ctx.else_stmt() else None
        return reduce(lambda acc, ele: If(ele.expr, ele.thenStmt, acc), y, z)

    def visitOnly_if_stmt(self,ctx:MiniGoParser.Only_if_stmtContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.block()), None)
    
    def visitElse_if_list(self,ctx:MiniGoParser.Else_if_listContext):
        return [self.visit(x) for x in ctx.only_if_stmt()]
    
    def visitElse_stmt(self,ctx:MiniGoParser.Else_stmtContext):
        return self.visit(ctx.block())
    
    # For Statement
    def visitFor_stmt(self,ctx:MiniGoParser.For_stmtContext):
        return self.visit(ctx.getChild(0))
    
    # Basic For Loop
    def visitBasic_for_stmt(self,ctx:MiniGoParser.Basic_for_loopContext):
        return ForBasic(self.visit(ctx.expr()), self.visit(ctx.block()))
    
    # For Loop with Initialization, Condition, and Update
    def visitFor_loop_initial(self,ctx:MiniGoParser.For_loop_initialContext):
        return ForStep(self.visit(ctx.initialization()), self.visit(ctx.expr()), self.visit(ctx.update()), self.visit(ctx.block()))
    
    def visitInitialization(self,ctx:MiniGoParser.InitializationContext):
        if ctx.update():
            return self.visit(ctx.update())
        else:
            return VarDecl(ctx.IDENTIFIER().getText(),
                       self.visit(ctx.typ()) if ctx.typ() else None,
                       self.visit(ctx.expr()))
    
    def visitUpdate(self,ctx:MiniGoParser.UpdateContext):
        lhs = Id(ctx.IDENTIFIER().getText())
        rhs = self.visit(ctx.expr())
        op = ctx.assign_operator().getText()
        if op == ':=':
            return Assign(lhs, rhs)
        else:
            return Assign(lhs, BinaryOp(op[0], lhs, rhs))

    # For Loop with Range
    def visitFor_loop_range(self,ctx:MiniGoParser.For_loop_rangeContext):
        return ForEach(Id(ctx.IDENTIFIER(0).getText()), Id(ctx.IDENTIFIER(1).getText()), self.visit(ctx.expr()), self.visit(ctx.block()))
        
    # Break Statement
    def visitBreak_stmt(self,ctx:MiniGoParser.Break_stmtContext):
        return Break()
    
    # Continue Statement
    def visitContinue_stmt(self,ctx:MiniGoParser.Continue_stmtContext):
        return Continue()
    
    # Call Statement
    def visitCall_stmt(self,ctx:MiniGoParser.Call_stmtContext):
        return CallStmt(self.visit(ctx.getChild(0)))
    
    # Return Statement
    def visitReturn_stmt(self,ctx:MiniGoParser.Return_stmtContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)

    # Function
    # Function declaration
    def visitFunc_decl(self,ctx:MiniGoParser.Func_declContext):
        return FuncDecl(ctx.IDENTIFIER().getText(),
                        self.visit(ctx.param_list()) if ctx.param_list() else [],
                        self.visit(ctx.typ()) if ctx.typ() else VoidType(),
                        self.visit(ctx.block()))
    
    # Function call
    def visitFunc_call(self,ctx:MiniGoParser.Func_callContext):
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.argument_list()) if ctx.argument_list() else [])
    
    def visitArgument_list(self,ctx:MiniGoParser.Argument_listContext):
        return [self.visit(x) for x in ctx.expr()]
    
    # Method
    # Method declaration
    def visitMethod_decl(self,ctx:MiniGoParser.Method_declContext):
        funcDecl = FuncDecl(ctx.IDENTIFIER(2).getText(),
                        self.visit(ctx.param_list()) if ctx.param_list() else [],
                        self.visit(ctx.typ()) if ctx.typ() else VoidType(),
                        self.visit(ctx.block()))
        return MethodDecl(ctx.IDENTIFIER(0).getText(), Id(ctx.IDENTIFIER(1).getText()), funcDecl)
    
    # Method call
    def visitMethod_call(self,ctx:MiniGoParser.Method_callContext):
        funcCall = self.visit(ctx.func_call())
        return MethodCall(self.visit(ctx.expr6()), funcCall.funName, funcCall.args)
    
    # Type
    def visitPrimitive_type(self,ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():    
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return BoolType()
        
    def visitTyp(self,ctx:MiniGoParser.TypContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.getChild(0))